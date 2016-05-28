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
      .when '/traders_sh',
        templateUrl: 'views/traders_stakeholders.html'
        controller: 'TradersCtrl'
      .when '/traders_p',
        templateUrl: 'views/traders_public.html'
        controller: 'TradersCtrl'
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
