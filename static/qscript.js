// $(document).ready(function() {
//     $('.click_button').click(function() {
//         var button_id = $(this).attr('id');
//         // Send a POST request to the Flask route with the button ID
//         $.ajax({
//             url: '/button_click',
//             type: 'POST',
//             data: {button_id: button_id},
//             success: function(response) {
//                 $('.caption2').append('<p>' + response + '</p>');
//             },
//             error: function(error) {
//                 console.log(error);
//             }
//         });
//     });
// });
$(document).ready(function() {
    $('.click_button').click(function() {
        var button_id = $(this).attr('id');
        var grandparentDiv = $(this).parent().parent(); // Get the grandparent div of the button
        var listContainer = grandparentDiv.find('.caption2'); // Get the container for the lists

        // Check if there is an existing unordered list
        var existingList = listContainer.find('ul');

        // Send a POST request to the Flask route with the button ID
        $.ajax({
            url: '/button_click',
            type: 'POST',
            data: {button_id: button_id},
            success: function(response) {
                console.log(response);
                if (response.length == 0) {
                    // If no response, display "No Replies"
                    if (existingList.length) {
                        existingList.replaceWith('<ul><li>No Replies</li></ul>'); // Replace existing list with a paragraph
                    } else {
                        // If no existing list, append a paragraph
                        listContainer.append('<ul><li>No Replies</li></ul>');
                    }
                } else {
                    // If there is a response
                    var newList = '<ul>'; // Start a new unordered list

                    response.forEach(function(reply) {
                        newList += '<li>' + reply + '</li>'; // Add each reply as a list item
                    });

                    newList += '</ul>'; // End of the unordered list

                    if (existingList.length) {
                        existingList.replaceWith(newList); // Replace existing list with the new one
                    } else {
                        listContainer.append(newList); // Append the new list if no existing list
                    }
                }
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});


