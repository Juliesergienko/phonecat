angular.module('phonecatFilters', []).filter('checkmark', function() {
  return function(input) {
  	yes = "postal code exists: " +input
  	no = "no postal code"
    return input ? yes : no;
  };
});