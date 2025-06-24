const open = document.getElementById('open');

open.onclick = () => {
    showModal();
};

function showModal() {
    // 모달창 껍데기(div) 만들기
    const modalWrapper = document.createElement('div');
    modalWrapper.className = 'modal-wrapper';

    // 다 하나하나 만들기 귀찮아서, 모달창 안에 내용을 html로 채워넣기
    modalWrapper.innerHTML = `
        <div class="modal">
            <div class="modal-title">모달 타이틀</div>
            <p>모달 본문 내용 Lorem ipsum dolor sit amet consectetur adipisicing elit. Assumenda repellendus mollitia necessitatibus voluptatum cumque iste, harum nam, nihil deserunt, rerum eligendi! Praesentium quibusdam quaerat nobis veniam hic doloribus omnis culpa?</p>
            <div class="close-wrapper">
                <button id="close">닫기버튼</button>
            </div>
        </div>
    `;

    // body에다가 위에 만든 모달창 껍데기를 붙이기
    document.body.appendChild(modalWrapper);

    // 닫기 버튼 이벤트 추가
    // const close = document.getElementById('close');
    // close.onclick = () => {
    //     modalWrapper.remove();
    // }

    // JS는 짧고 간결하게 짜려는 다양한 문법과 기법들이 있음...
    document.getElementById('close').onclick = () => {
        modalWrapper.remove();
    }
}
