'use strict';

/* Controllers */

angular.module('myApp.controllers', []).
  controller('AppCtrl', function ($scope, $http) {

    $http({
      method: 'GET',
      url: '/api/name'
    }).
    success(function (data, status, headers, config) {
      $scope.name = data.name;
    }).
    error(function (data, status, headers, config) {
      $scope.name = 'Error!'
    });

  }).
  controller('MyCtrl1', function ($scope,elasticService) {
    $scope.results = elasticService.getArray();
    $scope.data = "";

    $scope.search = function(){
        elasticService.search($scope.data);
        $scope.results = elasticService.getArray();
    }
  }).
  controller('MyCtrl2', function ($scope) {
    // write Ctrl here

  });
