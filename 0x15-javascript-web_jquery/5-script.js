// Add A New Element To A List

$('div#add_item').click(function () {
  const element = '<li>Item</li>';
  $('ul.my_list').append(element);
});
