const slider = document.getElementById('volume-slider');
const mainDisplay = document.getElementById('main-vol-display');
const pendingText = document.getElementById('pending-vol-text');

const overlay = document.getElementById('modal-overlay');
const stepConfirm = document.getElementById('step-confirm');
const stepCaptcha = document.getElementById('step-captcha');
const stepSuccess = document.getElementById('step-success');
const checkbox = document.getElementById('fake-checkbox');

let currentVolume = 50;
let pendingVolume = 50;

slider.addEventListener('change', (e) => {
    pendingVolume = e.target.value;
    pendingText.innerText = pendingVolume;
    
    overlay.classList.add('active');
    showStep(stepConfirm);
});

function cancelChange() {
    slider.value = currentVolume;
    overlay.classList.remove('active');
}

function goToCaptcha() {
    showStep(stepCaptcha);
    checkbox.classList.remove('checked');
}

function verifyCaptcha() {
    checkbox.classList.add('checked');
    
    setTimeout(() => {
        showStep(stepSuccess);

        setTimeout(() => {
            currentVolume = pendingVolume;
            mainDisplay.innerText = currentVolume;
            overlay.classList.remove('active');
        }, 1500);
        
    }, 600);
}

function showStep(stepElement) {
    stepConfirm.classList.remove('active');
    stepCaptcha.classList.remove('active');
    stepSuccess.classList.remove('active');
    
    stepElement.classList.add('active');
}