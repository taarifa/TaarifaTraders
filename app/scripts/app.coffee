'use strict'

app = angular
  .module('taarifaWaterpointsApp', [
    'ui.bootstrap'
    'gridster',
    'ngResource',
    'ngRoute',
    'ngCookies',
    'dynform',
    'angular-flash.service',
    'angular-flash.flash-alert-directive',
    'geolocation',
    'gettext',
  ])

  .config ($routeProvider, $httpProvider, flashProvider) ->
    $routeProvider
      #.when '/',
       # templateUrl: 'views/main.html'
       # controller: 'MainCtrl'
       # reloadOnSearch: false
     #.when '/waterpoints/edit/:id',
       # templateUrl: 'views/edit.html'
       # controller: 'WaterpointEditCtrl'
     #.when '/traders/new',
       # templateUrl: 'views/edit.html'
       # controller: 'TradersCreateCtrl'
     #.when '/dashboard',
       # templateUrl: 'views/dashboard.html'
       # controller: 'DashboardCtrl'
      .when '/',
        templateUrl: 'views/login.html'
        controller: 'LoginCtrl'
      .when '/subscribers',
        templateUrl: 'views/subscribers.html'
        controller: 'SubscribersCtrl'
      .when '/traders',
        templateUrl: 'views/traders.html'
        controller: 'TradersCtrl'
      .when '/test',
        templateUrl: 'views/test.html'
        controller: 'TestCtrl'
      .otherwise
        redirectTo: '/'
    $httpProvider.defaults.headers.patch =
      'Content-Type': 'application/json;charset=utf-8'
    flashProvider.errorClassnames.push 'alert-danger'

  .filter('titlecase', () -> 
    return (s) -> 
      return s.toString().toLowerCase().replace( /\b([a-z])/g, (ch) -> return ch.toUpperCase()))

  .run ($rootScope, flash) ->
    $rootScope.$on '$locationChangeSuccess', ->
      # Clear all flash messages on route change
      flash.info = ''
      flash.success = ''
      flash.warn = ''
      flash.error = ''
