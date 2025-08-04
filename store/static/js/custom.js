$(document).ready(function () {

    // Increment button
    $('.increment-btn').click(function (e) {
        e.preventDefault();

        var $input = $(this).closest('.product_data').find('.qty-input');
        var currentValue = parseInt($input.val(), 10);
        var maxValue = parseInt($input.attr('max'), 10); // Read max stock

        currentValue = isNaN(currentValue) ? 0 : currentValue;
        maxValue = isNaN(maxValue) ? 10 : maxValue;

        if (currentValue < maxValue) {
            currentValue++;
            $input.val(currentValue);
        }
    });

    // Decrement button
    $('.decrement-btn').click(function (e) {
        e.preventDefault();

        var $input = $(this).closest('.product_data').find('.qty-input');
        var currentValue = parseInt($input.val(), 10);

        currentValue = isNaN(currentValue) ? 0 : currentValue;

        if (currentValue > 1) {
            currentValue--;
            $input.val(currentValue);
        }
    });

    // Add to cart
    $('.addtocartbtn').click(function (e) {
        e.preventDefault();

        var product_id = $(this).closest('.product_data').find('.prod_id').val();
        var product_qty = $(this).closest('.product_data').find('.qty-input').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();

        $.ajax({
            method: "POST",
            url: "/add-to-cart/",
            data: {
                'product_id': product_id,
                'product_qty': product_qty,
                csrfmiddlewaretoken: token
            },
            success: function (response) {
                alertify.success(response.status);
            }
        });
    });

    // Update cart quantity
    $('.update-cart-btn').click(function (e) {
        e.preventDefault();

        var product_id = $(this).closest('.product_data').find('.prod_id').val();
        var product_qty = $(this).closest('.product_data').find('.qty-input').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();

        $.ajax({
            method: "POST",
            url: "/update-cart/",
            data: {
                'product_id': product_id,
                'product_qty': product_qty,
                csrfmiddlewaretoken: token
            },
            success: function (response) {
                alertify.success(response.status);
            }
        });
    });

    // Delete cart item
    $('.delete-cart-item').click(function (e) {
        e.preventDefault();

        var product_id = $(this).closest('.product_data').find('.prod_id').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();

        $.ajax({
            method: "POST",
            url: "/delete-cart-item",
            data: {
                'product_id': product_id,
                csrfmiddlewaretoken: token
            },
            success: function (response) {
                alertify.success(response.status);
                $('.cartdata').load(location.href + " .cartdata");
            }
        });
    });

    // Add to wishlist
    $('.addtowishlistbtn').click(function (e) {
        e.preventDefault();

        var product_id = $(this).closest('.product_data').find('.prod_id').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();

        $.ajax({
            method: "POST",
            url: "/add-to-wishlist/",
            data: {
                'product_id': product_id,
                csrfmiddlewaretoken: token
            },
            success: function (response) {
                console.log("Response from server:", response);
                alertify.success(response.status);
            }
        });
    });

    // Delete wishlist item
    $('.delete-wishlist-item').click(function (e) {
        e.preventDefault();

        var product_id = $(this).closest('.product_data').find('.prod_id').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();

        $.ajax({
            method: "POST",
            url: "/delete-wishlist-item/",
            data: {
                'product_id': product_id,
                csrfmiddlewaretoken: token
            },
            success: function (response) {
                alertify.success(response.status);
                $('.wishdata').load(location.href + " .wishdata");
            }
        });
    });

});
