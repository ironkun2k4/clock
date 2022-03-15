import QrScanner from "./qr-scanner/qr-scanner.min.js";
const video = document.getElementById('qr-video');
const videoContainer = document.getElementById('video-container');
const camList = document.getElementById('cam-list');
const camQrResult = document.getElementById('cam-qr-result');
const memberId = document.getElementById('member-id');
const submitButton = document.getElementById('submit-btn');

function setResult(label, result) {
    console.log(result.data);
    label.textContent = result.data;
    label.style.color = 'teal';
    clearTimeout(label.highlightTimeout);
    label.highlightTimeout = setTimeout(() => label.style.color = 'inherit', 100);

    if (result.data.startsWith("LYN")) {
        memberId.setAttribute('value', result.data);
        document.getElementById('form').style.display = 'block';
    }
}

// Web Cam Scanning
const scanner = new QrScanner(video, result => setResult(camQrResult, result), {
    onDecodeError: error => {
        camQrResult.textContent = error;
        camQrResult.style.color = 'inherit';
    },
    highlightScanRegion: true,
    highlightCodeOutline: true,
});

scanner.start().then(() => {
    QrScanner.listCameras(true).then(cameras => cameras.forEach(camera => {
        const option = document.createElement('option');
        option.value = camera.id;
        option.text = camera.label;
        camList.add(option);
    }));
});

// for debugging
window.scanner = scanner;

document.getElementById('inversion-mode-select').addEventListener('change', event => {
    scanner.setInversionMode(event.target.value);
});

camList.addEventListener('change', event => {
    scanner.setCamera(event.target.value);
});
