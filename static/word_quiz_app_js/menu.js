document.addEventListener('DOMContentLoaded', () => {
    $menu_btn = document.querySelector('.menu-button');
    $menu_opt = document.querySelector('.menu-options');
    
    $menu_btn.addEventListener('click', e => {
        $menu_btn.classList.toggle('menu-open');
        $menu_opt.classList.toggle('menu-open');
    })
})