### Project Overview

Project Overview:

This project aims to create a Location-based Partner Network platform with the following key features:

1. Location-based Partner Network: The platform will display ACLEDA's partners and merchants on a map, making it convenient for customers to locate nearby transaction points. Additionally, it will integrate partner data to showcase real-time promotions and offers.

2. Customizable Branding: Banks and financial institutions will have the ability to personalize the platform by adding their logos, colors, and branding elements to the map. This customization will provide a tailored experience to their customers.

3. Transaction History Visualization: Customers will be able to visualize their transaction history on the map, gaining insights into their spending patterns and financial behaviors.

4. Financial Services Hotspots: The platform will identify areas with high demand for financial services based on factors such as population density and customer demographics. This information will assist banks in identifying potential locations for new branches, ATMs, and self-service kiosks.

In summary, this project aims to develop a versatile platform that enhances customer experience by facilitating the discovery of transaction locations, offers branding customization options for financial institutions, provides insights into transaction history, and assists in strategic expansion based on demand analytics.

We utilize Node Package Manager (NPM) as a central tool to streamline project actions, making it easier to develop, test, and maintain two interconnected components: an API and a web UI.

### Project Components:

- API Component: This component is responsible for providing the back-end functionality of the application. It includes server-side logic, database interactions, and API endpoints. By housing it within the Monoripo monorepo, developers can work on it independently, allowing for modular development and testing.

- Web UI Component: The web UI component represents the user-facing part of the application. It includes all the front-end code, such as HTML, CSS, JavaScript, and any necessary client-side libraries or frameworks. Just like the API component, it is housed within the monorepo, enabling developers to manage the front-end and back-end codebase together seamlessly.

### Installation Guide
### To use the Monoripo, you need to install Node.js and Docker with Docker Compose.
Once you have installed the above and have cloned the repository, you can follow the following steps to get the project up and running:
1. Run `npm run build` to build docker image for merchant-api
2. Run `npm run start` then it will start all project in packages folder 

### Merchant-Api Features

- Python 3.11+ support
- SQLAlchemy 2.0+ support
- Asynchoronous capabilities
- Database migrations using Alembic
- Basic Authentication using JWT
- Row Level Access Control for permissions
- Redis for caching
- Celery for background tasks
- Testing suite
- Type checking using mypy
- Dockerized database and redis
- Readily available CRUD operations
- Linting using pylint
- Formatting using black

The project is designed to be modular and scalable. There are 3 main directories in the project:

1. `core`: This directory contains the central part of this project. It contains most of the boiler plate code like security dependencies, database connections, configuration, middlewares etc. It also contains the base classes for the models, repositories, and controllers. The `core` directory is designed to be as minimal as possible and usually requires minimal attention. Overall, the `core` directory is designed to be as generic as possible and can be used in any project. While building additional feature you may not need to modify this directory at all except for adding more controllers to the `Factory` class in `core/factory.py`.

2. `app`: This directory contains the actual application code. It contains the models, repositories, controllers, and schemas for the application. This is the directory you will be spending most of your time in while building features. The directory has following sub-directories:

   - `models` Here is where you add new tables
   - `repositories` For each model, you need to create a repository. This is where you add the CRUD operations for the model.
   - `controllers` For each logical unit of the application, you need to create a controller. This is where you add the business logic for the application.
   - `schemas` This is where you add the schemas for the application. The schemas are used for validation and serialization/deserialization of the data.

3. `api`: This directory contains the API layer of the application. It contains the API router, it is where you add the API endpoints.
#### Repository Pattern

The boilerplate uses the repository pattern. Every model has a repository and all of them inherit `base` repository from `core/repository`. The repositories are located in `app/repositories`. The repositories are injected into the controllers inside the `Factory` class in `core/factory/factory.py.py`.

The base repository has the basic crud operations. All customer operations can be added to the specific repository. Example:

```python
from core.repository import BaseRepository
from app.models.user import User
from sqlalchemy.sql.expression import select

class UserRepository(BaseRepository[User]):
    async def get_by_email(self, email: str):
        return await select(User).filter(User.email == email).gino.first()

```

To facilitate easier access to queries with complex joins, the `BaseRepository` class has a `_query` function (along with other handy functions like `_all()` and `_one_or_none()`) which can be used to write compplex queries very easily. Example:

```python
async def get_user_by_email_join_tasks(email: str):
    query = await self._query(join_)
    query = query.filter(User.email == email)
    return await self._one_or_none(query)
```

Note: For every join you want to make you need to create a function in the same repository with pattern `_join_{name}`. Example: `_join_tasks` for `tasks`. Example:

```python
async def _join_tasks(self, query: Select) -> Select:
    return query.options(joinedload(User.tasks))
```

#### Controllers

Kind of to repositories, every logical unit of the application has a controller. The controller also has a primary repository which is injected into it. The controllers are located in `app/controllers`.

These controllers contain all the business logic of the application. Check `app/controllers/auth.py` for an example.

#### Schemas

The schemas are located in `app/schemas`. The schemas are used to validate the request body and response body. The schemas are also used to generate the OpenAPI documentation. The schemas are inherited from `BaseModel` from `pydantic`. The schemas are primarily isolated into `requests` and `responses` which are pretty self explainatory.

#### Formatting

You can use `make format` to format the code using `black` and `isort`.

#### Linting

You can use `make lint` to lint the code using `pylint`.

#### Testing

The project contains tests for all endpoints, some of the logical components like `JWTHander` and `AccessControl` and an example of testing complex inner components like `BaseRepository`. The tests are located in `tests/`. You can run the tests using `make test`.

## Acknowledgements

- This project derived from [iam-abbas/FastAPI-Production-Boilerplate](https://github.com/iam-abbas/FastAPI-Production-Boilerplate)