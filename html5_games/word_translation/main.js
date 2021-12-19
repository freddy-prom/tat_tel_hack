var items = [
    'абитуриент', 'абитуриент',
    'абунә, абонемент', 'абонемент',
    'бунәче', 'абонент - абонент',
    'абориген', 'абориген',
    'бергәләп, бергәләшеп', 'заодно',
    'читтән торып укучы', 'заочник',
    'зебра', 'зебра',
    'йоткылык тамак', 'зев',
    'игенчелек, зирәгатьчелек', 'земледелие',
    'җир    казучы (эшче)', 'землекоп',
    'җирсоскыч, комсоскыч', 'землечерпалка',
    'сәламәтлекне саклау', 'здравоохранение',
];

$.onload = function () {
    $.get('https://23.111.122.227:5000/api/v1/dictionary/words/random/1', function (resp) {
        console.log(resp)
    });
}
var current = 0;
var timer;
var bonus = 0;
var record = 0;
var bestRecord = 0;

//setItem(current);
WindowAspectUpdate();

window.onresize = function () {
    WindowAspectUpdate();
}

document.getElementById('begin').onclick = function () {
    record = 0;
    document.getElementById('mainAnswers').style.display = 'block';
    document.getElementById('helloModal').style.display = 'none';
    setItem();
}

document.querySelector('form').onsubmit = function () {
    checkItem(document.querySelector('input').value);
    current++;
    setItem();

    return false;
}


function WindowAspectUpdate() {
    if (window.innerWidth < window.innerHeight) {
        document.getElementById('content').style.width = '100%';
        document.getElementById('mainAnswers').style.transform = 'translate(-50%, -50%) scale(3)';
        document.getElementById('helloModal').style.transform = 'translate(-50%, -50%) scale(2.5)';
    } else {
        document.getElementById('content').style.width = '50%';
        document.getElementById('mainAnswers').style.transform = 'translate(-50%, -50%) scale(1.5)';
        document.getElementById('helloModal').style.transform = 'translate(-50%, -50%) scale(1.3)';
    }
}

function checkItem(value) {
    if (value == items[current * 2 + 1]) {
        alert('Правильно');
        document.getElementById('progress').innerHTML = 'Рекорд: ' + (record++)
        bonus = 2;
    } else {
        alert('Неправильно');
        if (bonus >= 0) {
            bonus = -2;
        } else {
            bonus -= 2;
        }
    }
}

function setItem() {
    document.getElementById('progress-bar').style.transition = 'width 0s linear';
    document.getElementById('progress-bar').style.width = '100%';
    setTimeout(function () {
        document.querySelector('input').value = '';
        document.getElementById('progress-bar').style.transition = 'width ' + (10 + bonus) + 's linear';
        document.getElementById('progress-bar').style.width = '0%';
        if (timer != undefined) {
            window.clearTimeout(timer);
        }
        console.log(10 + bonus);
        updateTimer(10 + bonus);
    }, 500);
    document.getElementById('extra_info').innerHTML = 'Дайте перевод слову - <b>' + items[current * 2] + '</b>';
}

function updateTimer(value) {
    document.getElementById('progress-bar').innerHTML = value + 'c';
    if (value - 1 >= 0) {
        timer = setTimeout(() => {
            updateTimer(value - 1)
        }, 1000);
    } else {
        alert('Время вышло!');
        if (record > bestRecord) {
            bestRecord = record;
            document.getElementById('bestProgress').innerHTML = 'Лучший результат: ' + bestRecord;
        }
        current = 0;
        document.getElementById('mainAnswers').style.display = 'none';
        document.getElementById('helloModal').style.display = 'block';
    }
}

