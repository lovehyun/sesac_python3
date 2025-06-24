const open = document.getElementById('open');
const close = document.getElementById('close');

// const modal = document.getElementsByClassName('modal-wrapper')[0];
const modal = document.querySelector('.modal-wrapper')

// open.onclick = function openModal() {
// }

// open.onclick = function () {
// }

// 이거 포함 위에 3가지가 다 같은거다!!
open.onclick = () => {
    modal.style.display = 'flex';
}

close.onclick = () => {
    modal.style.display = 'none';
}
