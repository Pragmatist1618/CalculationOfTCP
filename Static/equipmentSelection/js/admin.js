(function($){
    $(document).ready(function(){
        // Изменение события при изменении производителя
        $('#id_supplier').on('change', function(){
            // Определите значение производителя Siemens
            var siemensManufacturerId = '1';
            var selectedManufacturerId = $(this).val();

            // Получение элемента поля model
            var modelField = $('#id_model');

            // Показать или скрыть поле в зависимости от выбранного производителя
            if (selectedManufacturerId == siemensManufacturerId) {
                modelField.closest('.form-row').show();
            } else {
                modelField.val('');
                modelField.closest('.form-row').hide();
            }
        });

        // Вызов события изменения производителя, чтобы установить начальное состояние
        $('#id_supplier').trigger('change');
    });
})(django.jQuery);