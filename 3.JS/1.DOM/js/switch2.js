document.addEventListener('DOMContentLoaded', function () {
    // 여기는 브라우저가 DOM을 다 불러왔을때 여기가 호출됨.
    let fruitSelector = document.getElementById('fruitSelector');
    fruitSelector.addEventListener('change', function () {
        // 이게 실행될 내용을 여기 추가...
        console.log('변경감지됨');
    });

    fruitSelector.addEventListener('change', fruitDisplay);
});

function fruitDisplay() {
    let fruit = document.getElementById('fruitSelector').value;
    let result = document.getElementById('fruitResult');
    // if (fruit === "apple") {
    //     result.innerText = "이것은 사과입니다.";
    // } else if (fruit === "banana") {
    //     result.innerText = "이것은 바나나입니다.";
    // } else {
    //      result.innerTExt = "아몰랑";
    // }

    // 이 switch/case 는 언제나 if/else 로 대체는 가능함.
    // 하지만, 가독성이 좋게 하기 위해서 생겨난 문법.
    // case 가 끝났을때는 break가 없으면, 아래로 쭉 흘러가서 다 처리한다.
    switch (fruit) {
        case 'apple':
        case 'APPLE':
            result.innerText = '이것은 사과입니다.';
            break;
        case 'banana':
        case 'BANANA':
            result.innerText = '<B>이것은 바나나입니다.</B>';
            break;
        case 'orange':
        case 'ORANGE':
            result.innerHTML = '이것은 오렌지입니다.';
            break;
        case 'pineapple':
        case 'PINEAPPLE':
            result.innerHTML = '<B>이것은 파인애플입니다.</B>';
            break;
        default:
            result.textContent = '<B>아몰랑</B>';
    }
}
