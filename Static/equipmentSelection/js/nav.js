$(document).ready(function () {
    $('.block:not(.active)').hide();

    // Обработка события клика по ссылке
    $('.nav-link').on('click', function () {
        if (!$(this).hasClass('dropdown-toggle')) {
            // Получаем идентификатор блока, который нужно показать
            var targetBlockId = $(this).data('target');
            // console.log(targetBlockId)

            $('.nav-link').removeClass('active');
            // Добавляем класс 'active' только к текущей ссылке
            $(this).addClass('active');

            // Скрываем все блоки
            $('.block').removeClass('active');
            $('.block').hide();

            // Показываем только выбранный блок
            $('#' + targetBlockId).addClass('active');
            $('#' + targetBlockId).show();
        }
    });
});