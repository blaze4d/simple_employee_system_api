# Simple Employee Management System
A simple employee management system API with activity logging

# REST API
The REST API is described below

## Get API Overview
This displays the available APIs
### Request
`GET /api`
### Response
	HTTP 200 OK
	Allow: GET, OPTIONS
	Content-Type: application/json
	Vary: Accept
	{
		"List": "/api/employee-list/",
		"Detail View": "/api/employee-detail/<str:id>/",
		"Create": "/api/employee-create/",
		"Update": "/api/employee-update/",
		"Archive": "/api/employee-archive/<str:id>/"
	}
## Get Employee List
This retrieves the list of all employees
### Request
`GET /api/employee-list`
### Response
	HTTP 200 OK
	Allow: GET, OPTIONS
	Content-Type: application/json
	Vary: Accept

	[
		{
			"id": 1,
			"first_name": "James",
			"last_name": "Curry",
			"date_employed": "2015-10-12",
			"salary_level": 6,
			"department": "Admin",
			"last_promotion_date": null
		},
		{
			"id": 2,
			"first_name": "John",
			"last_name": "Fisher",
			"date_employed": "2017-06-19",
			"salary_level": 5,
			"department": "HR",
			"last_promotion_date": "2019-06-30"
		}
	]
## Get Employee Detail
This retrieves the detail of an employee. Returns a 404 if id not found
### Request
`GET /api/employee-detail/<id>`
### Response
	HTTP 200 OK
	Allow: GET, OPTIONS
	Content-Type: application/json
	Vary: Accept

	{
		"id": 1,
		"first_name": "James",
		"last_name": "Curry",
		"date_employed": "2012-10-12",
		"salary_level": 6,
		"department": "Account",
		"last_promotion_date": null
	}
## Add Employee
Add employee to the system
### Request
`POST /api/employee-create/`

	{
		"first_name": "Charles",
		"last_name": "Freeman",
		"date_employed": "2018-10-12",
		"salary_level": 4,
		"department": "Data Processing"
	}

### Response
	HTTP 200 OK
	Allow: POST, OPTIONS
	Content-Type: application/json
	Vary: Accept
	{
		"id": 3,
		"first_name": "Charles",
		"last_name": "Freeman",
		"date_employed": "2018-10-12",
		"salary_level": 4,
		"department": "Data Processing"
		"last_promotion_date": null
	}

  ## Update Employee
Update an employee detail
### Request
`POST /api/employee-update/1`

	{
		"first_name": "James",
		"last_name": "Curry",
		"date_employed": "2012-10-12",
		"salary_level": 6,
		"department": "Account",
		"last_promotion_date": "2015-06-08"
	}
### Response
	HTTP 200 OK
	Allow: POST, OPTIONS
	Content-Type: application/json
	Vary: Accept
	{
		"id": 1,
		"first_name": "James",
		"last_name": "Curry",
		"date_employed": "2012-10-12",
		"salary_level": 6,
		"department": "Account",
		"last_promotion_date": "2015-06-08"
	}

  
## Archive Employee
Archive an employee detail
### Request
`DELETE /api/employee-archive/3`
### Response
	HTTP 200 OK
	Allow: DELETE, OPTIONS
	Content-Type: application/json
	Vary: Accept
"Employee archived successfully"

## View Activity Logs
View activity logs
### Request
`Get /api/log-list`
### Response
	HTTP 200 OK
	Allow: GET, OPTIONS
	Content-Type: application/json
	Vary: Accept
	HTTP 200 OK
	Allow: OPTIONS, GET
	Content-Type: application/json
	Vary: Accept

	[
			{
					"id": 3,
					"action_time": "2020-11-19T11:23:54.101558Z",
					"object_id": "9",
					"object_repr": "John Finsher",
					"action_flag": 1,
					"change_message": "[{\"added\": {}}]",
					"user": 1,
					"content_type": 7
			},
			{
					"id": 2,
					"action_time": "2020-11-19T10:14:57.461078Z",
					"object_id": "8",
					"object_repr": "Caren Flower",
					"action_flag": 1,
					"change_message": "[{\"added\": {}}]",
					"user": 1,
					"content_type": 7
			},
			{
					"id": 1,
					"action_time": "2020-11-19T09:00:29.797699Z",
					"object_id": "7",
					"object_repr": "James Nwoke",
					"action_flag": 1,
					"change_message": "[{\"added\": {}}]",
					"user": 1,
					"content_type": 7
			}
	]
