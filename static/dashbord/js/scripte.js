let btn = document.querySelector('#btn');
let nav = document.querySelector('.sidebar');
let dbnon = document.querySelectorAll('.sidebar ul li a span');
let dbinput = document.querySelector('.sidebar ul li a input');
let icons = document.querySelectorAll('.sidebar ul li a i');
let logoname = document.querySelector('.logocontent'); 
let imglft = document.querySelector('#prfimg');
let namdb = document.querySelector('.name_gamer');
let logout = document.querySelector('.bxs-log-out');
let shearch = document.querySelector('.bx-search-alt-2');
let relogo = document.querySelector('.profilcontent');
let contentre = document.querySelector('.home_content');
btn.addEventListener('click',
function () {
    nav.classList.toggle('navDesactive');
    dbnon.forEach(function (e) {
        e.classList.toggle('dsbnonre');
    })
    btn.classList.toggle('rsizebtn')
    icons.forEach(function (e) {
        e.classList.toggle('pdt5');
    })
    dbinput.classList.toggle('dsbnonre');
    logoname.classList.toggle('dsbnonre');
    imglft.classList.toggle('mglft4');
    namdb.classList.toggle('dsbnonre');
    logout.classList.toggle('dsbnonre');
    shearch.classList.toggle('bgtransparnt');
    relogo.classList.toggle('bgtransparnt');
    contentre.classList.toggle('home_contentresize');
}

)