var phonecatControllers = angular.module('phonecatControllers', []);

phonecatControllers.controller('PhoneListCtrl', ['$http', '$scope', '$log', function ($http, $scope, $log) {
  	$log.debug("In list controller")
  	$http.get('/address').success(function(response){
  		$scope.address = response;
  		$log.debug($scope.address);
  		});
  	$scope.orderProp = "postalcity";
  	$scope.add_new = function(){
  		$log.debug("new address:")
  		$log.debug($scope.new_address)
  		  		$http.put('/address/' +$scope.new_address.userseqno, $scope.new_address).success(function(){
  			$log.debug("Success!")
  			})
  		.error(function(){
  			$log.debug("Error while putting a new address into db")
  			});
  		}
  	$scope.select_items = [ {text: 'Name', value: 'address'}, 
  		{text: 'Id', value: 'userseqno'}, {text: 'City', value: 'postalcity'} ];
  	
  	
  }]);



  
  phonecatControllers.controller( 'PhoneDetailCtrl', ['$scope', '$http', '$log', '$window', '$routeParams', 
  	function($scope, $http, $log, $window, $routeParams){
  		$log.debug("In detail controller")
  	$scope.addressId = $routeParams.addressId;
  	$log.debug("you are on the other page");

  	$scope.delete_address = function(){
  		$log.debug("this address will be deleted")
  		$http.delete('/address/'+$scope.addressId).success(
  			function(){
  				$log.debug("deleted successfully");
  			})
  		.error(function(){
  			$log.debug("didn't delete")
  		})

  	}
  	function get_info(){
  		$http.post('/address',{}, {params:{"id":$scope.addressId}}).success(
  			function(data){
  				$log.debug(data)
  				$scope.show_info = data
  			})
  		.error(function(){
  			$log.debug("Error recieving info about certain address")
  		})
  	}

  	get_info()
  }]);