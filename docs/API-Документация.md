# Transport Company API

API для управления транспортной компанией

# Base URL


| URL | Description |
|-----|-------------|


# Authentication



## Security Schemes

| Name              | Type              | Description              | Scheme              | Bearer Format             |
|-------------------|-------------------|--------------------------|---------------------|---------------------------|
| jwtAuth | http |  | bearer | JWT |

# APIs

## POST /api/auth/drivers/create/



Создание водителя - ТОЛЬКО для админов




### Request Body

[CreateUser](#createuser)





[CreateUser](#createuser)





[CreateUser](#createuser)







### Responses

#### 201



[CreateUser](#createuser)







## POST /api/auth/login/



Вход для админов и водителей




### Request Body

[MyTokenObtainPair](#mytokenobtainpair)





[MyTokenObtainPair](#mytokenobtainpair)





[MyTokenObtainPair](#mytokenobtainpair)







### Responses

#### 200



[MyTokenObtainPair](#mytokenobtainpair)







## GET /api/auth/me/



Получить данные текущего пользователя




### Responses

#### 200



[UserShort](#usershort)







## POST /api/auth/token/refresh/



Takes a refresh type JSON web token and returns an access type JSON web
token if the refresh token is valid.




### Request Body

[TokenRefresh](#tokenrefresh)





[TokenRefresh](#tokenrefresh)





[TokenRefresh](#tokenrefresh)







### Responses

#### 200



[TokenRefresh](#tokenrefresh)







## POST /api/auth/token/verify/



Takes a token and indicates if it is valid.  This view provides no
information about a token's fitness for a particular use.




### Request Body

[TokenVerify](#tokenverify)





[TokenVerify](#tokenverify)





[TokenVerify](#tokenverify)







### Responses

#### 200



[TokenVerify](#tokenverify)







## GET /api/bookings/



ViewSet для работы с бронированиями - только для администраторов




### Responses

#### 200



array







## POST /api/bookings/



ViewSet для работы с бронированиями - только для администраторов




### Request Body

[Booking](#booking)





[Booking](#booking)





[Booking](#booking)







### Responses

#### 201



[Booking](#booking)







## GET /api/bookings/{id}/



ViewSet для работы с бронированиями - только для администраторов


### Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| id | string | True |  |


### Responses

#### 200



[Booking](#booking)







## PUT /api/bookings/{id}/



ViewSet для работы с бронированиями - только для администраторов


### Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| id | string | True |  |


### Request Body

[Booking](#booking)





[Booking](#booking)





[Booking](#booking)







### Responses

#### 200



[Booking](#booking)







## PATCH /api/bookings/{id}/



ViewSet для работы с бронированиями - только для администраторов


### Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| id | string | True |  |


### Request Body

[PatchedBooking](#patchedbooking)





[PatchedBooking](#patchedbooking)





[PatchedBooking](#patchedbooking)







### Responses

#### 200



[Booking](#booking)







## DELETE /api/bookings/{id}/



ViewSet для работы с бронированиями - только для администраторов


### Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| id | string | True |  |


### Responses

#### 204


No response body




## GET /api/customers/customers/





### Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| ordering | string | False | Which field to use when ordering the results. |
| search | string | False | A search term. |


### Responses

#### 200



array







## POST /api/customers/customers/







### Request Body

[Customer](#customer)





[Customer](#customer)





[Customer](#customer)







### Responses

#### 201



[Customer](#customer)







## GET /api/customers/customers/{id}/





### Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| id | string | True |  |


### Responses

#### 200



[Customer](#customer)







## PUT /api/customers/customers/{id}/





### Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| id | string | True |  |


### Request Body

[Customer](#customer)





[Customer](#customer)





[Customer](#customer)







### Responses

#### 200



[Customer](#customer)







## PATCH /api/customers/customers/{id}/





### Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| id | string | True |  |


### Request Body

[PatchedCustomer](#patchedcustomer)





[PatchedCustomer](#patchedcustomer)





[PatchedCustomer](#patchedcustomer)







### Responses

#### 200



[Customer](#customer)







## DELETE /api/customers/customers/{id}/





### Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| id | string | True |  |


### Responses

#### 204


No response body




## GET /api/customers/customers/organizations/



Путь для получения только организаций




### Responses

#### 200



[Customer](#customer)







## GET /api/drivers/driver-profiles/





### Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| ordering | string | False | Which field to use when ordering the results. |
| search | string | False | A search term. |


### Responses

#### 200



array







## POST /api/drivers/driver-profiles/







### Request Body

[DriverProfileCreate](#driverprofilecreate)





[DriverProfileCreate](#driverprofilecreate)





[DriverProfileCreate](#driverprofilecreate)







### Responses

#### 201



[DriverProfileCreate](#driverprofilecreate)







## GET /api/drivers/driver-profiles/{id}/





### Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| id | string | True |  |


### Responses

#### 200



[DriverProfile](#driverprofile)







## PUT /api/drivers/driver-profiles/{id}/





### Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| id | string | True |  |


### Request Body

[DriverProfileCreate](#driverprofilecreate)





[DriverProfileCreate](#driverprofilecreate)





[DriverProfileCreate](#driverprofilecreate)







### Responses

#### 200



[DriverProfileCreate](#driverprofilecreate)







## PATCH /api/drivers/driver-profiles/{id}/





### Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| id | string | True |  |


### Request Body

[PatchedDriverProfileCreate](#patcheddriverprofilecreate)





[PatchedDriverProfileCreate](#patcheddriverprofilecreate)





[PatchedDriverProfileCreate](#patcheddriverprofilecreate)







### Responses

#### 200



[DriverProfileCreate](#driverprofilecreate)







## DELETE /api/drivers/driver-profiles/{id}/





### Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| id | string | True |  |


### Responses

#### 204


No response body




## POST /api/public/booking/



Публичный эндпоинт для формы заявки на сайте (без авторизации)




### Request Body

[BookingPublic](#bookingpublic)





[BookingPublic](#bookingpublic)





[BookingPublic](#bookingpublic)







### Responses

#### 201



[BookingPublic](#bookingpublic)







## GET /api/vehicles/vehicles/





### Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| ordering | string | False | Which field to use when ordering the results. |
| search | string | False | A search term. |


### Responses

#### 200



array







## POST /api/vehicles/vehicles/







### Request Body

[VihicleCreate](#vihiclecreate)





[VihicleCreate](#vihiclecreate)





[VihicleCreate](#vihiclecreate)







### Responses

#### 201



[VihicleCreate](#vihiclecreate)







## GET /api/vehicles/vehicles/{id}/





### Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| id | string | True |  |


### Responses

#### 200



[Vehicle](#vehicle)







## PUT /api/vehicles/vehicles/{id}/





### Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| id | string | True |  |


### Request Body

[VihicleCreate](#vihiclecreate)





[VihicleCreate](#vihiclecreate)





[VihicleCreate](#vihiclecreate)







### Responses

#### 200



[VihicleCreate](#vihiclecreate)







## PATCH /api/vehicles/vehicles/{id}/





### Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| id | string | True |  |


### Request Body

[PatchedVihicleCreate](#patchedvihiclecreate)





[PatchedVihicleCreate](#patchedvihiclecreate)





[PatchedVihicleCreate](#patchedvihiclecreate)







### Responses

#### 200



[VihicleCreate](#vihiclecreate)







## DELETE /api/vehicles/vehicles/{id}/





### Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| id | string | True |  |


### Responses

#### 204


No response body




# Components



## AccountTypeEnum


* `ADMIN` - Администратор
* `DRIVER` - Водитель




## Booking


Для администраторов через API - полная информация


| Field | Type | Description |
|-------|------|-------------|
| id | string | Уникальный идентификатор |
| customer |  |  |
| source |  | Откуда поступила заявка

* `PHONE` - Телефон
* `EMAIL` - Email
* `WEBSITE` - Сайт
* `MESSENGER` - Мессенджер |
| desired_trip_date | string | Дата когда клиент хочет совершить поездку |
| desired_departure_time | string | Время отправления по желанию клиента |
| arrival_location | string | Адрес или название пункта назначения |
| passenger_count | integer | Сколько человек планируют поездку |
| luggage_description | string | Информация о количестве и типе багажа |
| status |  | Текущий статус бронирования

* `NEW` - Новая
* `CONFIRMED` - Подтверждена
* `IN_PROGRESS` - В работе
* `COMPLETED` - Завершена
* `CANCELLED` - Отменена |
| notes | string | Дополнительные заметки и пожелания |
| created_at | string | Автоматически устанавливается при создании |
| updated_at | string | Автоматически обновляется при каждом сохранении |


## BookingPublic


Для формы заявки на сайте (анонимные пользователи)


| Field | Type | Description |
|-------|------|-------------|
| customer_name | string |  |
| customer_phone | string |  |
| customer_email | string |  |
| desired_trip_date | string | Дата когда клиент хочет совершить поездку |
| desired_departure_time | string | Время отправления по желанию клиента |
| arrival_location | string | Адрес или название пункта назначения |
| passenger_count | integer | Сколько человек планируют поездку |
| luggage_description | string | Информация о количестве и типе багажа |
| notes | string | Дополнительные заметки и пожелания |


## BookingStatusEnum


* `NEW` - Новая
* `CONFIRMED` - Подтверждена
* `IN_PROGRESS` - В работе
* `COMPLETED` - Завершена
* `CANCELLED` - Отменена




## CategoryEnum


* `BUS` - Автобус
* `MINIBUS` - Микроавтобус




## CreateUser



| Field | Type | Description |
|-------|------|-------------|
| email | string | Email адрес для входа в систему |
| password | string |  |


## Customer



| Field | Type | Description |
|-------|------|-------------|
| id | string | Уникальный идентификатор |
| contact_person_name | string |  |
| organization_name | string | Название компании (если клиент - организация) |
| phone | string | Контактный номер телефона |
| email | string | Адрес электронной почты |
| customer_type |  | Физическое лицо или организация

* `INDIVIDUAL` - Физическое лицо
* `ORGANIZATION` - Организация |
| is_deleted | boolean | Отметка о мягком удалении записи |
| created_at | string | Автоматически устанавливается при создании |
| updated_at | string | Автоматически обновляется при каждом сохранении |


## CustomerTypeEnum


* `INDIVIDUAL` - Физическое лицо
* `ORGANIZATION` - Организация




## DriverPayment



| Field | Type | Description |
|-------|------|-------------|
| id | string | Уникальный идентификатор |
| driver | string | Уникальный идентификатор |
| driver_name | string |  |
| payment_date | string | Дата фактической выплаты |
| period_start | string | Дата начала расчетного периода |
| period_end | string | Дата окончания расчетного периода |
| days_worked | integer | Автоматически вычисляется на основе периода |
| base_amount | string | Автоматически вычисляется: дни × ставка |
| bonus_amount | string | Дополнительная премия (в рублях) |
| bonus_reason | string | Описание за что выплачен бонус |
| total_amount | string | Автоматически вычисляется: базовая сумма + бонус |
| notes | string | Дополнительные заметки о выплате |


## DriverProfile



| Field | Type | Description |
|-------|------|-------------|
| id | string | Уникальный идентификатор |
| user |  |  |
| phone | string | Контактный номер телефона водителя |
| license_number | string | Уникальный номер ВУ |
| license_category | string | Категория водительского удостоверения (например, D, D1) |
| hire_date | string | Дата приема на работу |
| status |  | Текущий статус водителя

* `ACTIVE` - Активен
* `INACTIVE` - Неактивен
* `ON_VACATION` - В отпуске |
| daily_rate | string | Оплата за один рабочий день (в рублях) |
| payments | array |  |


## DriverProfileCreate



| Field | Type | Description |
|-------|------|-------------|
| email | string |  |
| phone | string | Контактный номер телефона водителя |
| license_number | string | Уникальный номер ВУ |
| license_category | string | Категория водительского удостоверения (например, D, D1) |
| hire_date | string | Дата приема на работу |
| status |  | Текущий статус водителя

* `ACTIVE` - Активен
* `INACTIVE` - Неактивен
* `ON_VACATION` - В отпуске |
| daily_rate | string | Оплата за один рабочий день (в рублях) |


## MyTokenObtainPair



| Field | Type | Description |
|-------|------|-------------|
| email | string |  |
| password | string |  |


## PatchedBooking


Для администраторов через API - полная информация


| Field | Type | Description |
|-------|------|-------------|
| id | string | Уникальный идентификатор |
| customer |  |  |
| source |  | Откуда поступила заявка

* `PHONE` - Телефон
* `EMAIL` - Email
* `WEBSITE` - Сайт
* `MESSENGER` - Мессенджер |
| desired_trip_date | string | Дата когда клиент хочет совершить поездку |
| desired_departure_time | string | Время отправления по желанию клиента |
| arrival_location | string | Адрес или название пункта назначения |
| passenger_count | integer | Сколько человек планируют поездку |
| luggage_description | string | Информация о количестве и типе багажа |
| status |  | Текущий статус бронирования

* `NEW` - Новая
* `CONFIRMED` - Подтверждена
* `IN_PROGRESS` - В работе
* `COMPLETED` - Завершена
* `CANCELLED` - Отменена |
| notes | string | Дополнительные заметки и пожелания |
| created_at | string | Автоматически устанавливается при создании |
| updated_at | string | Автоматически обновляется при каждом сохранении |


## PatchedCustomer



| Field | Type | Description |
|-------|------|-------------|
| id | string | Уникальный идентификатор |
| contact_person_name | string |  |
| organization_name | string | Название компании (если клиент - организация) |
| phone | string | Контактный номер телефона |
| email | string | Адрес электронной почты |
| customer_type |  | Физическое лицо или организация

* `INDIVIDUAL` - Физическое лицо
* `ORGANIZATION` - Организация |
| is_deleted | boolean | Отметка о мягком удалении записи |
| created_at | string | Автоматически устанавливается при создании |
| updated_at | string | Автоматически обновляется при каждом сохранении |


## PatchedDriverProfileCreate



| Field | Type | Description |
|-------|------|-------------|
| email | string |  |
| phone | string | Контактный номер телефона водителя |
| license_number | string | Уникальный номер ВУ |
| license_category | string | Категория водительского удостоверения (например, D, D1) |
| hire_date | string | Дата приема на работу |
| status |  | Текущий статус водителя

* `ACTIVE` - Активен
* `INACTIVE` - Неактивен
* `ON_VACATION` - В отпуске |
| daily_rate | string | Оплата за один рабочий день (в рублях) |


## PatchedVihicleCreate



| Field | Type | Description |
|-------|------|-------------|
| brand | string | Марка транспортного средства (например, Mercedes) |
| model | string | Модель транспортного средства (например, Sprinter) |
| year | integer | Год производства транспортного средства |
| license_plate | string | Регистрационный номер транспортного средства |
| capacity | integer | Количество пассажирских мест |
| category |  | Тип транспортного средства

* `BUS` - Автобус
* `MINIBUS` - Микроавтобус |


## SourceEnum


* `PHONE` - Телефон
* `EMAIL` - Email
* `WEBSITE` - Сайт
* `MESSENGER` - Мессенджер




## Status663Enum


* `ACTIVE` - Активен
* `INACTIVE` - Неактивен
* `ON_VACATION` - В отпуске




## TokenRefresh



| Field | Type | Description |
|-------|------|-------------|
| access | string |  |
| refresh | string |  |


## TokenVerify



| Field | Type | Description |
|-------|------|-------------|
| token | string |  |


## UserShort



| Field | Type | Description |
|-------|------|-------------|
| id | string | Уникальный идентификатор |
| email | string | Email адрес для входа в систему |
| full_name | string |  |
| avatar | string | Фотография профиля пользователя |
| account_type |  | Роль пользователя в системе

* `ADMIN` - Администратор
* `DRIVER` - Водитель |
| is_active | boolean | Активен ли аккаунт пользователя |


## Vehicle



| Field | Type | Description |
|-------|------|-------------|
| id | string | Уникальный идентификатор |
| brand | string | Марка транспортного средства (например, Mercedes) |
| model | string | Модель транспортного средства (например, Sprinter) |
| year | integer | Год производства транспортного средства |
| license_plate | string | Регистрационный номер транспортного средства |
| capacity | integer | Количество пассажирских мест |
| category |  | Тип транспортного средства

* `BUS` - Автобус
* `MINIBUS` - Микроавтобус |
| is_active | boolean | Доступен ли транспорт для использования |
| created_at | string | Автоматически устанавливается при создании |
| updated_at | string | Автоматически обновляется при каждом сохранении |


## VihicleCreate



| Field | Type | Description |
|-------|------|-------------|
| brand | string | Марка транспортного средства (например, Mercedes) |
| model | string | Модель транспортного средства (например, Sprinter) |
| year | integer | Год производства транспортного средства |
| license_plate | string | Регистрационный номер транспортного средства |
| capacity | integer | Количество пассажирских мест |
| category |  | Тип транспортного средства

* `BUS` - Автобус
* `MINIBUS` - Микроавтобус |
