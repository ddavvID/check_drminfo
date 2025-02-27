## Detailed Explanation of Widevine DRM and HDCP

**Widevine DRM**

Overview

Widevine DRM is a digital rights management system developed by Widevine Technologies and acquired by Google.

It is widely used by streaming services like Netflix and Amazon Prime Video to protect premium content from unauthorized access and piracy.

<img width="500" alt="image" src="https://github.com/user-attachments/assets/b4f94b2b-ac30-4f3a-9d53-8dceea2ed47b" />



## Security Levels

Widevine DRM has three security levels: **L1**, **L2**, and **L3**. These levels differ in their security and decryption capabilities.

L1：This is the highest security level. Content is decrypted within a Trusted Execution Environment (TEE) on the device, ensuring hardware-level protection against data leakage. L1 is required for high-quality video streaming services like Netflix and Amazon Prime Video. Devices with L1 certification can play high-definition and ultra-high-definition content.

L2：Offers a high level of security but is less stringent than L1. Encryption operations are performed within the TEE, but content processing may not be. L2 devices can still play high-quality content, though not as high as L1.

L3：The lowest security level. Content processing and encryption occur outside the TEE, often using software-based methods. This level is typically used for lower-resolution content or on devices that do not support TEE. The maximum resolution supported is usually 480p.

## HDCP

Overview

HDCP (High-Bandwidth Digital Content Protection) is a digital rights management system designed to protect digital content transmitted over interfaces like HDMI, DisplayPort, and DVI. It encrypts digital signals to prevent unauthorized copying or interception during transmission.

### HDCP Versions

HDCP has two main versions: **1.x** and **2.x**.

* Primarily used for Full HD (1080p) content. It is widely supported by older devices but lacks the advanced security features of newer versions.
* Introduced for higher resolutions like 4K (3840×2160 or 4096×2160). HDCP 2.2 and 2.3 are the latest versions, offering enhanced security and compatibility with newer devices. HDCP 2.x is not backward compatible with HDCP 1.x.

### Workflow

1.  The source device and receiving device authenticate each other to ensure both support HDCP.
2.  The source device encrypts the digital signal before transmission.
3.  The receiving device decrypts the signal and plays it back.

| Feature              | Widevine DRM                 | HDCP                                   |
| :------------------- | :--------------------------- | :------------------------------------- |
| Application          | Online streaming services    | Digital interfaces (HDMI, DVI)         |
| Protection Method    | Encryption and license management | Signal encryption during transmission |
| Security Level       | L1 > L2 > L3                 | HDCP 2.x offers higher security than HDCP 1.x |
| Version Compatibility | Not applicable               | HDCP 2.x is not compatible with HDCP 1.x |

In summary, Widevine DRM focuses on protecting online content through encryption and licensing, with varying security levels (L1, L2, L3) to ensure different qualities of streaming.

HDCP protects content transmitted over digital interfaces by encrypting the signal, with HDCP 2.x offering better security for higher resolutions.

## Introduction to H.264 and H.265

## H.264

* **Standard Name**: H.264, also known as MPEG-4 AVC, is a video compression standard jointly developed by ISO and ITU-T.
* **Compression Efficiency**: H.264 has a high compression ratio, offering better efficiency than MPEG-2 and MPEG-4.
* **Applications**: Suitable for standard definition and high-definition video transmission, providing a smooth video experience at low bitrates.
* **Limitations**: May not be efficient enough for resolutions above 4K.

## H.265

* **Standard Name**: H.265, also known as HEVC (High Efficiency Video Coding), is the successor to H.264.
* **Compression Efficiency**: H.265 offers about twice the compression efficiency of H.264, reducing the bitrate by 50% for the same video quality.
* **Applications**: Supports 4K and 8K ultra-high-definition videos, ideal for high-resolution video transmission and storage.
* **Advantages**: Provides higher quality video experiences under limited bandwidth, supporting higher frame rates and color depths.

## Key Differences

| Feature              | H.264                        | H.265                               |
| :------------------- | :--------------------------- | :---------------------------------- |
| Compression Efficiency | High, but less than H.265    | Approximately twice that of H.264 |
| Supported Resolution | High Definition (720P/1080P) | 4K, 8K Ultra-HD                     |
| Application Scenarios | Standard and High Definition Videos | High-Resolution Video Transmission and Storage |
| Storage Space        | Relatively larger            | Reduces by 50% for the same quality |

## Bitrate Ranges

* **H.264**:
    * **720P (1280x720)**: 1,500 kbps to 5,000 kbps
    * **1080P (1920x1080)**: 3,000 kbps to 10,000 kbps
* **H.265**:
    * **720P (1280x720)**: 1,000 kbps to 3,500 kbps
    * **1080P (1920x1080)**: 2,000 kbps to 6,000 kbps

These ranges are based on general applications and platforms (such as YouTube), and actual requirements may vary depending on the complexity of the video content and playback demands.

H.265 typically offers similar or better video quality at lower bitrates, making it increasingly popular for high-resolution videos.

## Supported browsers and WebView for each DRM

* Browsers
    * Widevine
        * Chrome and Opera for Android 5+
        * Chrome, Firefox and Opera for Windows 7+, macOS 10.12+ and Linux
        * MS Edge 79+ for Windows 7+
        * Chrome for ChromeOS
        * Latest Amazon Silk for fireOS 6+
    * PlayReady
        * MS Edge 79+ for Windows 7+
        * MS Edge Legacy for Windows 7+
    * FairPlay
        * Safari on iOS 10+ and iPadOS 13+
        * Safari for macOS 10.12+
* Android & iOS mobile apps (Ionic, Flutter, Apache Cordova, WebView)
    * Widevine: Android 7+
    * FairPlay: WKWebView for iOS 13+ and iPadOS 13+
* OTT apps
    * Widevine
        * Samsung Smart TV apps (Tizen 3+)
        * LG Smart TV apps (webOS 3+)
        * Desktop apps with Electron 6+
        * Google Cast receiver application

## Most environments should support L1 level with Widevine DRM, including:

### Chrome and WebView for Android

### Samsung and LG Smart TV

**There is however one notable exception: Chrome and Firefox for Desktop (Windows or macOS) only offer L3 Google Widevine security level (software DRM).**

## How Does Widevine DRM Work?

In Widevine DRM, secure decryption is done via a series of exchanges between the Content Decryption Module and the Widevine DRM license server.

The HTML5 video player acts as a mediator for these exchanges. Although, by itself, the player cannot read the encrypted license or video.

<img width="628" alt="image" src="https://github.com/user-attachments/assets/57e08838-e48a-4179-92c2-84ec175f568e" />


1.  **Video is received from the CDN or Content Delivery Network**
2.  **Browser’s media engine identifies whether the video is encrypted or not**
    1.  When you press the play button, the browser’s media engine will identify whether the video is encrypted or not.
3.  **Initialization data is sent to the License Proxy**
    1.  After identifying it, 'initData' or initialization data is taken by the browser and sent to the License Proxy.
4.  **License Proxy sends the data to the License Service**
    1.  The License Proxy sends the data to the License Service.
5.  **License Service processes the request and returns the license to the License Proxy**
    1.  The License Service receives the request from the License Proxy and sends the license back to the License Proxy.
6.  **License Proxy sends the license to the Media Player**
    1.  The License Proxy sends the license to the Media Player.
7.  **Media Player sends the license to the CDM (Content Decryption Module)**
    1.  The Media Player sends the license to the CDM.
8.  **CDM sends the data to the OEMCrypto HAL**
    1.  The CDM sends the data to the OEMCrypto HAL.
9.  **OEMCrypto HAL decrypts the data**
    1.  The OEMCrypto HAL decrypts the data.
10. **Decrypted video chunks are sent from the OEMCrypto HAL to the Media Player**
    1.  The decrypted video chunks are sent from the OEMCrypto HAL to the Media Player.
11. **Media Player plays the video on the client device**
    1.  After the video is decrypted and decoded, it is then sent to the Media Player in small chunks. The viewer is able to play the video, and security is also ensured. And voila, you get video playback on your device.
   
sorce: https://developers.google.com/widevine?hl=zh-tw
       https://www.radiantmediaplayer.com/docs/v9/dash-drm-documentation.html#robustness-widevine
       https://docs.gumlet.com/reference/widevine-drm
