import pytest
import subprocess
import re

# 測試配置
DEFAULT_VIDEO_ID = "87sLC6Ys"

# Helper functions
def get_connected_devices():
    """
    偵測已連線的 Android 設備，返回設備 ID 列表
    """
    try:
        process = subprocess.run(
            ["adb", "devices"],
            capture_output=True,
            text=True,
            check=True
        )
        output = process.stdout
        devices = []
        for line in output.splitlines():
            if "device" in line and "devices" not in line:
                device_id = line.split("\t")[0]
                devices.append(device_id)
        return devices
    except subprocess.CalledProcessError as e:
        pytest.fail(f"偵測設備失敗: {e}")

def get_widevine_level(device_id):
    """
    獲取指定 Android 设备的 Widevine DRM Level
    """
    try:
        process = subprocess.run(
            ["adb", "-s", device_id, "shell", "dumpsys", "media.drm"],
            capture_output=True,
            text=True,
            check=True
        )
        output = process.stdout
        # 使用更寬鬆的正則表達式來匹配 DRM Level
        match = re.search(r"securityLevel:\s*(L[123]|L1|L2|L3)", output)
        if match:
            level = match.group(1).strip()
            return level
        else:
            print("未找到 DRM Level")
            return None
    except subprocess.CalledProcessError as e:
        pytest.fail(f"獲取 DRM Level 失敗: {e}")

def get_hdcp_status(device_id):
    """
    獲取指定 Android 设备的 HDCP 状态
    """
    try:
        process = subprocess.run(
            ["adb", "-s", device_id, "shell", "dumpsys", "display"],
            capture_output=True,
            text=True,
            check=True
        )
        output = process.stdout
        # 使用更寬鬆的正則表達式來匹配 HDCP 版本號
        match = re.search(r"HDCP:\s*(\d+\.?\d*)", output)
        if match:
            status = match.group(1).strip()
            return status
        else:
            print("未找到 HDCP 狀態")
            return None
    except subprocess.CalledProcessError as e:
        pytest.fail(f"獲取 HDCP 狀態失敗: {e}")

@pytest.fixture(scope="session")
def connected_devices():
    """
    獲取所有已連線的 Android 設備，作為 fixture
    """
    devices = get_connected_devices()
    
    if not devices:
        pytest.fail("未找到已連線的 Android 設備")
    
    return devices

def test_drm_hdcp_verification(connected_devices):
    """
    測試 DRM Level 和 HDCP 驗證，支持單個或多個設備。
    """
    
    for device_id in connected_devices:
        print(f"正在測試設備: {device_id}")
        
        # 1. 獲取 DRM Level 和 HDCP 等級
        try:
            drm_level = get_widevine_level(device_id)
            hdcp_status = get_hdcp_status(device_id)

            # 打印設備信息
            print(f"已連接設備: {device_id} 的 DRM Level: {drm_level}, HDCP 狀態: {hdcp_status}")

        except Exception as e:
            pytest.fail(f"在設備 {device_id} 上發生錯誤: {e}")
