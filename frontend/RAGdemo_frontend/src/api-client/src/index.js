/**
 * FastAPI
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from './ApiClient';
import DBQueryModel from './model/DBQueryModel';
import HTTPValidationError from './model/HTTPValidationError';
import SubmitQueryRequest from './model/SubmitQueryRequest';
import ValidationError from './model/ValidationError';
import ValidationErrorLocInner from './model/ValidationErrorLocInner';
import DefaultApi from './api/DefaultApi';


/**
* JS API client generated by OpenAPI Generator.<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var FastApi = require('index'); // See note below*.
* var xxxSvc = new FastApi.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new FastApi.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* <em>*NOTE: For a top-level AMD script, use require(['index'], function(){...})
* and put the application logic within the callback function.</em>
* </p>
* <p>
* A non-AMD browser application (discouraged) might do something like this:
* <pre>
* var xxxSvc = new FastApi.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new FastApi.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version 0.1.0
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
     * The DBQueryModel model constructor.
     * @property {module:model/DBQueryModel}
     */
    DBQueryModel,

    /**
     * The HTTPValidationError model constructor.
     * @property {module:model/HTTPValidationError}
     */
    HTTPValidationError,

    /**
     * The SubmitQueryRequest model constructor.
     * @property {module:model/SubmitQueryRequest}
     */
    SubmitQueryRequest,

    /**
     * The ValidationError model constructor.
     * @property {module:model/ValidationError}
     */
    ValidationError,

    /**
     * The ValidationErrorLocInner model constructor.
     * @property {module:model/ValidationErrorLocInner}
     */
    ValidationErrorLocInner,

    /**
    * The DefaultApi service constructor.
    * @property {module:api/DefaultApi}
    */
    DefaultApi
};
