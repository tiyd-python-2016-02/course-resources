var $abilities = $('#abilities');

$.get('http://localhost:8000/abilities/', function(abilities){
  abilities.results.forEach(function(ability) {
    console.log(ability)
    var $li = $('<li>');
    $li.text(ability.name)
    $li.appendTo($abilities);
  })
})


var $ability = $('#ability');
var $name = $('input[name="name"]');
var $damage = $('input[name="damage"]');
var $rarity = $('input[name="rarity"]');
var $icon = $('input[name="icon"]');

$ability.submit(function() {
  console.log('you submitted the form');

  $.ajax({
    method: 'post',
    url: 'http://localhost:8000/abilities/',
    username: 'admin',
    password: 'password123',
    data: {
      name: $name.val(),
      damage: $damage.val(),
      icon: $icon.val(),
      rarity: $rarity.val()
    },
    success: function(newAbility) {
      console.log(newAbility)
      var $li = $('<li>');
      $li.text(newAbility.name)
      $li.appendTo($abilities);
    }
  });

  return false;
});
