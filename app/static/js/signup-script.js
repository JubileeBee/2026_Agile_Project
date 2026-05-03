// ── Password visibility toggles ──
function setupToggle(toggleId, inputId) {
    const btn = document.getElementById(toggleId);
    const input = document.getElementById(inputId);
    if (!btn || !input) return;
    btn.addEventListener('click', () => {
        const visible = input.type === 'text';
        input.type = visible ? 'password' : 'text';
        btn.classList.toggle('toggle-active', !visible);
    });
}
setupToggle('passwordToggle', 'password');
setupToggle('confirmToggle', 'confirmPassword');

// ── Password strength indicator ──
const pwInput       = document.getElementById('password');
const strengthBar   = document.getElementById('strengthBar');
const strengthLabel = document.getElementById('strengthLabel');
const segments      = ['seg1', 'seg2', 'seg3', 'seg4'].map(id => document.getElementById(id));
const labels        = ['', 'Weak', 'Fair', 'Good', 'Strong'];
const classes       = ['', 'active-weak', 'active-fair', 'active-good', 'active-strong'];

function getStrength(pw) {
    let score = 0;
    if (pw.length >= 8)          score++;
    if (/[A-Z]/.test(pw))        score++;
    if (/[0-9]/.test(pw))        score++;
    if (/[^A-Za-z0-9]/.test(pw)) score++;
    return score;
}

pwInput.addEventListener('input', () => {
    const pw = pwInput.value;
    if (!pw) {
        strengthBar.style.display = 'none';
        strengthLabel.textContent = '';
        segments.forEach(s => s.className = 'strength-segment');
        return;
    }
    strengthBar.style.display = 'flex';
    const score = getStrength(pw);
    segments.forEach((s, i) => {
        s.className = 'strength-segment' + (i < score ? ' ' + classes[score] : '');
    });
    strengthLabel.textContent = labels[score];
});

// ── Validation helpers ──
function showError(id, msg) {
    const el = document.getElementById(id);
    el.textContent = msg;
    el.classList.add('show');
    el.closest('.soft-field')?.classList.add('error');
}

function clearError(id) {
    const el = document.getElementById(id);
    el.textContent = '';
    el.classList.remove('show');
    el.closest('.soft-field')?.classList.remove('error');
}

// ── Form submission ──
document.getElementById('signupForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    let valid = true;

    ['firstNameError', 'lastNameError', 'emailError', 'passwordError', 'confirmError', 'termsError']
        .forEach(clearError);

    const firstName = document.getElementById('firstName').value.trim();
    const lastName  = document.getElementById('lastName').value.trim();
    const email     = document.getElementById('email').value.trim();
    const password  = document.getElementById('password').value;
    const confirm   = document.getElementById('confirmPassword').value;
    const terms     = document.getElementById('terms').checked;

    if (!firstName) { showError('firstNameError', 'First name is required.'); valid = false; }
    if (!lastName)  { showError('lastNameError',  'Last name is required.');  valid = false; }
    if (!email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
        showError('emailError', 'Please enter a valid email.'); valid = false;
    }
    if (password.length < 8) {
        showError('passwordError', 'Password must be at least 8 characters.'); valid = false;
    }
    if (password !== confirm) {
        showError('confirmError', 'Passwords do not match.'); valid = false;
    }
    if (!terms) {
        showError('termsError', 'Please accept the terms to continue.'); valid = false;
    }
    if (!valid) return;

    // Show loading spinner
    const btn = document.querySelector('.comfort-button');
    btn.classList.add('loading');

    // Replace this with your actual fetch/form submission logic e.g.:
    // const response = await fetch('/signup', { method: 'POST', ... });
    await new Promise(r => setTimeout(r, 1500));
    btn.classList.remove('loading');

    // Show success state
    document.getElementById('signupForm').style.display = 'none';
    document.querySelectorAll('.gentle-divider, .comfort-social, .comfort-signup')
        .forEach(el => el.style.display = 'none');
    const success = document.getElementById('successMessage');
    success.style.display = 'block';
    requestAnimationFrame(() => success.classList.add('show'));
});