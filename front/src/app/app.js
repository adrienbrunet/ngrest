import angular from 'angular';

import 'angular-animate';
import 'angular-touch';
import 'angular-ui-bootstrap';
import 'angular-formly';
import 'angular-formly-templates-bootstrap';

import 'bootstrap/dist/css/bootstrap.css';
import '../style/app.css';

import AppService from './service';
import AppCtrl from './controller';


let myComponent = {
  template: require('./app.html'),
  controller: AppCtrl,
};

const MODULE_NAME = 'app';

angular.module(MODULE_NAME, ['ui.bootstrap', 'formly', 'formlyBootstrap'])
  .component('app', myComponent)
  .service('AppService', AppService);

export default MODULE_NAME;
