# test_task

## To run 

### 1. Clone the Repository

First, clone the project repository from GitHub and navigate into the project directory:

```bash
git clone [https://github.com/molumolu-arch/task.git](https://github.com/molumolu-arch/task.git)
cd task
```

### 2. Run docker-compose
```bash
docker-compose up --build
```

### 3. Create superuser 
```bash
docker-compose exec django python manage.py createsuperuser
```

## Migrations 

* **`0001_initial.py`**: Sets up the custom `User` model, including a `coins` field and making `username` unique.
* **`0002_rewardlog_scheduledreward.py`**: Adds `RewardLog` (for tracking given rewards) and `ScheduledReward` (for future rewards) models.
* **`0003_user_request.py`**: Adds a `request` boolean field to the `User` model.
* **`0004_rewardrequestlog.py`**: Introduces the `RewardRequestLog` model to log user-initiated reward requests.
* **`0005_alter_model_options_alter_model_managers_etc.py`**:
    * Adjusts ordering options for `RewardLog` and `ScheduledReward`.
    * Removes the `request` field from the `User` model.
    * Updates timestamp handling for `given_at` and `requested_at` fields to `auto_now_add=True`.
    * Adds `related_name` attributes to foreign keys for better reverse relationships.
## EndPoints 

* `/api/token/`
* `/api/token/refresh/`
* `/api/token/verify/`
* `/api/profile/`
* `/api/rewards/`
* `/api/request/`
