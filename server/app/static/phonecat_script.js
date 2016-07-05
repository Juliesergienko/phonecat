var phonecatControllers = angular.module('phonecatControllers', []);

phonecatControllers.controller('PhoneListCtrl', ['$http', '$scope', '$log', function ($http, $scope, $log) {
  	$log.debug("In list controller")
  	$http.get('/address').success(function(response){
  		response = JSON.parse(response)
  		$log.debug(response);
  		$scope.address = []
  		angular.forEach(response, function(item){
  			$log.debug(item)
  			#########################################################3
  			dict = {"id":item[0], "address_type":item[1], "address":item[2],
  			"postal_code":item[3], "postal_city":item[4], "image":item[item.length-1]};
  			$scope.address.push(dict)
  		})
  		});
  	$scope.orderProp = "postal_city";
  	$scope.add_new = function(new_address){
  		$log.debug("will be given to server:")
  		$log.debug(new_address)
  		var dict = {"addresstype":new_address[0],
  		"address":new_address[0],
  		"postalcode":new_address[0],
  		"postalcity":new_address[0], 
  		"municipality":new_address[0],
  		"countrycode":new_address[0],
  		"userseqno":new_address[0]}
  		###################################################
  		  		$http.put('/address', dict).success(function(){
  			$log.debug("Success!")
  		})
  		.error(function(){
  			$log.debug("Error while putting a new address into db")
  		});
  	}
  	
  	
  }]);



  
  phonecatControllers.controller( 'PhoneDetailCtrl', ['$scope', '$http', '$log', '$window', '$routeParams', 
  	function($scope, $http, $log, $window, $routeParams){
  		$log.debug("In detail controller")
  	$scope.addressId = $routeParams.addressId;
  	$log.debug("you are on the other page");

  	$scope.back_to_main = function(){
  		$log.debug("button pressed")
  		$window.location.href = '#/';
  	}

  	$scope.delete_address = function(){
  		$log.debug("this address will be deleted")
  		$http.delete('/address', {params:{"id":$scope.addressId}}).success(
  			function(){
  				$log.debug("deleted successfully");
  				################################################################3
  				$window.location.href = '#/';
  			})
  		.error(function(){
  			$log.debug("didn't delete")
  		})

  	}
  	function get_info(){
  		$http.post('/address',{}, {params:{"id":$scope.addressId}}).success(
  			function(data){
  				data = JSON.parse(data)
  				$scope.show_info = data[0]
  			})
  		.error(function(){
  			$log.debug("Error recieving info about certain address")
  		})
  	}

  	get_info()
  }]);