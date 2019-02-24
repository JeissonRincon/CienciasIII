var app = angular.module("myApp", []);

app.controller("myCtrl", function($scope, $http) {
    $http.get('informacion.json')
     .then(function(res){
        $scope.informacion = res.data;
      });
});
