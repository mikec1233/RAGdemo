# FastApi.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getQueryEndpointGetQueryGet**](DefaultApi.md#getQueryEndpointGetQueryGet) | **GET** /get_query | Get Query Endpoint
[**listQueryEndpointListQueriesPost**](DefaultApi.md#listQueryEndpointListQueriesPost) | **POST** /list_queries | List Query Endpoint
[**submitQueryEndpointSubmitQueryPost**](DefaultApi.md#submitQueryEndpointSubmitQueryPost) | **POST** /submit_query | Submit Query Endpoint



## getQueryEndpointGetQueryGet

> DBQueryModel getQueryEndpointGetQueryGet(queryId)

Get Query Endpoint

### Example

```javascript
import FastApi from 'fast_api';

let apiInstance = new FastApi.DefaultApi();
let queryId = "queryId_example"; // String | 
apiInstance.getQueryEndpointGetQueryGet(queryId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **queryId** | **String**|  | 

### Return type

[**DBQueryModel**](DBQueryModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listQueryEndpointListQueriesPost

> [DBQueryModel] listQueryEndpointListQueriesPost(userId)

List Query Endpoint

### Example

```javascript
import FastApi from 'fast_api';

let apiInstance = new FastApi.DefaultApi();
let userId = "userId_example"; // String | 
apiInstance.listQueryEndpointListQueriesPost(userId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userId** | **String**|  | 

### Return type

[**[DBQueryModel]**](DBQueryModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## submitQueryEndpointSubmitQueryPost

> DBQueryModel submitQueryEndpointSubmitQueryPost(submitQueryRequest)

Submit Query Endpoint

### Example

```javascript
import FastApi from 'fast_api';

let apiInstance = new FastApi.DefaultApi();
let submitQueryRequest = new FastApi.SubmitQueryRequest(); // SubmitQueryRequest | 
apiInstance.submitQueryEndpointSubmitQueryPost(submitQueryRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submitQueryRequest** | [**SubmitQueryRequest**](SubmitQueryRequest.md)|  | 

### Return type

[**DBQueryModel**](DBQueryModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

