function number_inc() {
    console.log('증가버튼 클릭');
    let number = document.getElementById('result');
    let number_string = number.textContent;
    // DIV 요소 안에 있는 글을 가져오는 3가지 방식
    // innerText - 글자만 가져온다 (디자인 속성을 적용받음)
    // innerHTML - 글자와 그 태그까지 함께 가져온다
    // textContent - 순수 글자만 가져온다
    console.log(number_string);

    let number_string_to_number = Number(number_string);
    let result = number_string_to_number + 1;
    number.textContent = result;

    // 나의 생각이나 의도가 중요한게 아니고...
    // 내가 짠 코드 그 내용이 중요한것...
}

function number_dec() {
    // console.log("감소버튼 클릭");
    // 이거 구현하시오.....
    document.getElementById('result').textContent -= 1;
}
