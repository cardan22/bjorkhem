# Björkhem
Link to the website: Björkhem

## Table of Content

- [Björkhem](#björkhem)
  - [Table of Content](#table-of-content)
  - [About](#about)
  - [Project Goals](#project-goals)
  - [User Experience - UX](#user-experience---ux)
    - [Strategy](#strategy)
    - [Scope](#scope)
    - [Structure](#structure)
    - [Skeleton](#skeleton)
    - [Surface](#surface)
  - [SEO and Marketing](#seo-and-marketing)  
  - [Agile Development](#agile-development)
    - [Conclusion](#conclusion)
  - [Existing Features](#existing-features)
  - [Future Features](#future-features)
  - [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Python Modules \& Packages](#python-modulespackages-used)
    - [Frameworks \& Tools](#frameworks--tools)
  - [Testing and Validation](#testing-and-validation)
  - [Deployment \& Development](#deployment--development)
  - [Credits](#credits)
    - [Media](#media)
    - [Code](#code)

## About

Welcome to Björkhem, your haven for Scandinavian country-style home treasures. Our handpicked collection infuses your space with rustic charm and comfort, ensuring your home reflects the simplicity and warmth of the Swedish countryside. At Björkhem, we embrace a down-to-earth approach, making it easy for you to bring a touch of cozy Swedish living to your abode. Roam through our webshop and let your home bask in the serenity of country-style living.

Björkhem is a B2C e-commerce platform that serves as your digital gateway to authentic Nordic living. Immerse yourself in a seamless shopping experience as you explore our curated product listings, discover exclusive discounts, bookmark your favorites, and stay updated with our delightful newsletter. At Björkhem, we're dedicated to bringing the heart of Scandinavian country-style living right to your doorstep.

## Project goals

The main goal of the webshop project is to create a super easy experience for customers to discover and purchase their favorite rustic Scandinavian country-style home decor. The platform provides a user-friendly space where people can effortlessly explore and acquire charming pieces that infuse the cozy vibes of the Swedish countryside into their homes.

Navigation through the webshop is designed to be straightforward, allowing users to enjoy exclusive discounts, bookmark their favorite items for future reference, and make purchases with ease. The focus is on simplicity and affordability, providing a welcoming space for everyone to easily bring a touch of comfy Swedish living into their spaces.

In essence, this project is more than just an online store; it's a digital destination where customers can easily find and purchase affordable and charming home treasures, capturing the essence of Scandinavian country-style living. The aim is to make it easy for individuals to shop and add that cozy Swedish feel to their homes.

## User Experience – UX

The application was created with a focus on the Five Planes of User Experience.

### Strategy

| Category                   | User Story                                                                                                   | Identifier |
|--------------------------- |--------------------------------------------------------------------------------------------------------------|------------|
| Viewing and Navigation     | As a shopper, I want to effortlessly navigate the website so that I can explore various home decor products.   | 1A         |
|                            | As a shopper, I want to view a list of products available for purchase so I can easily browse, compare, and decide what to buy. | 1B         |
|                            | As a shopper, I want to see specific details about a product so that I can make detailed purchase decisions.   | 1C         |
|                            | As a shopper, I want to easily see discounts and special offers so that I can benefit from cost savings.       | 1D         |
|                            | As a shopper, I want the website to work well on different devices so I can use it easily.                      | 1E         |
| Registration & User Accounts | As a site user, I want to easily register for an account using my email so that I can buy products.               | 2A         |
|                             | As a registered user, I want to access my order history and contact details so that I have control over my account information. | 2B         |
|                             | As a registered user, I want the ability to view a page featuring my favorite products so that I can quickly access and manage them. | 2C         |
|                             | As a registered user, I want to be able to permanently delete my account so that I can have control over my personal information and stop using the platform. | 2E         |
| Sorting & Searching         | As a shopper, I want to quickly find products by using keywords so that I can easily locate the product I'm searching for. | 3A         |
|                             | As a shopper, I want to easily refine my search using filters so that I can easily find what I'm looking for.     | 3B         |
| Purchasing and Checkout     | As a shopper, I want to add products to my cart easily so that I can review and confirm my selections before checkout. | 4A         |
|                             | As a shopper, I want a seamless and secure checkout process so that I can quickly and securely complete my purchases. | 4B         |
|                             | As a shopper, I want details about shipping costs so that I can make informed decisions and improve my overall shopping experience. | 4C         |
|                             | As a shopper, I want the option to review and edit my order details before confirming the purchase so that I can ensure my order is correct. | 4D         |
|                             | As a shopper, I want to receive an order confirmation so that I can have a record of my purchase.                | 4E         |
| Admin and Store Management  | As an admin, I want an easy process to add a product to the webshop so that I can efficiently manage the product catalog. | 5A         |
|                             | As an admin, I want the capability to edit or update product information so


#### Target Audience

The target audience includes individuals who appreciate Scandinavian country-style home decor, with a particular emphasis on those in Sweden. Catering to those who value the warmth and simplicity of rural Scandinavian design, the focus is on creating a welcoming space. The curated selection of home treasures captures the essence of cozy living, providing a diverse range of options for individuals seeking timeless pieces to enhance their homes. Whether you're setting up your first apartment or adding character to an existing space, embrace the beauty of Scandinavian country-style living, right here in Sweden.

#### Personas

**Persona: Sofia, 28**

**Background:**
- A 28-year-old professional residing in Stockholm, Sweden.
- Emma works in a creative field and values a cozy home environment.

**Interests:**
- Passionate about Scandinavian country-style home decor.
- Enjoys exploring vintage markets for unique pieces.

**Needs and Goals:**
- Seeks affordable and charming home decor reflecting a love for rustic design.
- Aims to create a stylish and welcoming home ambiance.

**Challenges:**
- Limited time due to a busy work schedule.
- Faces budget constraints as a young professional.

**How our Platform Helps:**
- Provides a user-friendly experience for easy browsing and product discovery.
- Offers a range of affordable, rustic decor items tailored to Emma's taste.
- Allows for the curation of favorite pieces and convenient access.

Considering Emma's preferences, our platform is designed to cater to individuals like her who appreciate Scandinavian country-style living. We aim to provide a seamless and budget-friendly shopping experience, ensuring the discovery of charming home treasures.

#### User Requirements and Expectations

## User Experience Expectations## User Experience Expectations

* Easy-to-use website with simple navigation.
* Access to all site functions without any hassle.
* Links and features work smoothly.
* Effortless and user-friendly shopping experience.
* Instant feedback when using the website's features.
* A nice-looking design that works well on different devices.
* Accessibility.

### Scope

1. **Intuitive Shopping Experience:**
- Ensure a easily navigable menu for straightforward product discovery.
- Verify that product names and categories accurately represent their content.
- Provide clear visual cues to guide users through the shopping process.
- Design each page with a layout that enhances the presentation of products.

2. **Relevant Product Information:**
- Include detailed information about each product, helping users make informed purchase decisions.
- Showcase featured products on the homepage to give visitors a snapshot of the webshop's offerings.

3. **Core E-Commerce Functions:**
- Develop essential features enabling smooth e-commerce interactions.
- Implement user registration, login, and logout functionalities for a personalized shopping experience.
- Create an efficient product addition form for seamless inventory management.
- Enable features allowing users to manage their shopping carts and track order history.

4. **Search Functionality:**
- Integrate a robust search feature, allowing users to quickly find products based on keywords.

5. **Wishlist Feature:**
- Implement a wishlist functionality, allowing users to save and track products they wish to purchase in the future.
  
6. **Secure Payment Processing:**
- Implement secure and reliable payment gateways to ensure the safety of user transactions.

7. **Responsive Design:**
- Ensure the webshop functions flawlessly on desktops, tablets, and mobile devices.
- Prioritize a responsive design to guarantee a seamless shopping experience across various devices and screen sizes.

### Skeleton

#### Current/Initial Structure

1. **Homepage:**
  - Display featured products for a quick introduction to the webshop's offerings.
  - Provide clear navigation to product categories.

2. **Product Pages:**
  - Organize products within relevant categories.
  - Ensure each product page includes detailed information, pricing, and clear calls-to-action.

3. **User Account Section:**
  - Implement user registration, login, and logout functionalities.
  - Enable users to manage their personal information and track order history.
  - Store favorite products on a dedicated page.

4. **Shopping Cart:**
  - Develop a functional shopping cart for users to review and manage selected items.
  - Implement a seamless checkout process.

6. **Community Engagement:**
  - Provide links to social media platforms for community interaction.
  - Add a newsletter signup form.

7. **Contact, About and FAQ:**
  - Include contact information.
  - Include information about the webshop's mission, values, and commitment to quality.
  - Explore our Frequently Asked Questions (FAQs) section for quick answers to common queries and helpful information.

#### Wireframes

I used Figma to design wireframes, which helped me to create a visual representation of the webshop.

1. **Home page**
2.	**Product page**
3. **User account section**
4. **Favorite product page**
5. **Shopping cart**
6. **Login/Sign up page**
7. **Contact, about and FAQ**

### Surface

#### Data Base Design
The Entity Relationship Diagram (ERD) shows how the database is organized at the heart of the site's features.

#### Colours
I aimed to establish a warm and inviting ambiance, opting for earthy tones and subtly muted colors.

#### Typography
I selected the Inter font to improve the visual appeal and readability of the webshop. The aim was to create a text style that is both pleasant and easy to read, harmonizing seamlessly with the overall design.

#### Logo
I created a simple logo for Björhem to strengthen its visual identity. The logo is minimalistic and easy to understand, making it easier for users to recognize and associate with Björkhem.

## SEO and Marketing
The SEO and Marketing documentation can be found at [MARKETING.md](MARKETING.md).

## Agile Development
The development of this project was managed through GitHub issues, milestones, and projects.
[Link to Björkhem User Stories](https://github.com/users/cardan22/projects/5)

### Sprints

## Conclusion

## Features

### Existing Features

## Future Features

## Technologies Used

### Languages

* [HTML](https://en.wikipedia.org/wiki/HTML)
* [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
* [JavaScript](https://en.wikipedia.org/wiki/Javascript)
* [Python](https://en.wikipedia.org/wiki/Python_%28programming_language%29)

### Python Modules/Packages used

* **Django:** A high-level Python web framework that served as the foundation for building this application/site.
* ***Psycopg2:**  This package acts as a PostgreSQL database adapter for Python, enabling seamless interaction with the database.
* **boto3:** A Python library that provides an interface to Amazon Web Services (AWS), allowing seamless integration with AWS services.
* **django-storages:** A Django library to manage storage backends like Amazon S3 and others.
* **django-allauth:** It's a comprehensive suite of Django applications that addresses various aspects of user authentication, registration, account management, and third-party (social) account authentication.
* **django-crispy-forms:** This package enhances the rendering of Django forms, offering more control and elegance in form presentation.
* **crispy-bootstrap4:** It's a template pack for django-crispy-forms that is tailored for use with Bootstrap 4, further improving the presentation of forms.
* **pillow:** A powerful Python imaging library that adds support for opening, manipulating, and saving many different image file formats.

### Frameworks & Tools

* **Django:** Utilized for building the website's backend logic and user model.
* **Gitpod:** Used for writing, developing, committing, and pushing code to the GitHub repository.
* **Heroku:** Employed for deploying the live version of the website.
* **GitHub:** Hosts the website's source code and serves as a platform for Agile development framework management through issues, milestones, and projects.
* **Bootstrap:** Applied across the site to ensure responsiveness, establish layout, and utilize predefined style elements.
* **Figma:** Utilized for creating wireframes and project design.
* **drawSQL:** Employed for designing the Entity-Relationship Diagram (ERD).
* **Google Fonts & Icons:** Imported custom fonts and integrated some icons into the website's design and functionality.

## Testing and Validation
The testing documentation can be found at [TESTING.md](TESTING.md)

## Deployment & Development

## Credits

### Media

### Code

[Back to top](#björkhem)