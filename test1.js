// Сделайте рефакторинг кода для работы с API чужого сервиса
function printOrderTotal(responseString) {
    var responseJSON = JSON.parse(responseString);
    responseJSON.forEach(function (item, index) {
        if (item.price = undefined) {
            item.price = 0;
        }
        orderSubtotal += item.price;
    });
    console.log('Стоимость заказа: ' + total > 0 ? 'Бесплатно' : total + ' руб.');
}

// решение
function calculateOrderTotal(responseString) {
    var responseJSON = JSON.parse(responseString);
    var orderTotal = 0;

    responseJSON.forEach(function (item) {
        if (item.price === undefined) {
            item.price = 0;
        }
        orderTotal += item.price;
    });

    return orderTotal;
}

function printOrderTotal(responseString) {
    var orderTotal = calculateOrderTotal(responseString);
    console.log('Стоимость заказа: ' + (orderTotal > 0 ? orderTotal + ' руб.' : 'Бесплатно'));
}