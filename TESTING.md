# Björkhem Testing

:arrow_left: [Return to the README](README.md)

## Table of Contents

- [Performance](#performance)
- [Accessibility](#accessibility)
- [Code Validation](#code-validation)
  - [HTML Validation](#html-validation)
  - [CSS Validation](#css-validation)
  - [JS Validation](#js-validation)
  - [Python Validation](#python-validation)
- [Testing](#testing)
  - [Manual Testing](#manual-testing)
  - [Automated Testing](#automated-testing)
- [Browser Testing](#browser-testing)
- [Bugs & Fixes](#bugs-and-fixes)

# Performance
[Google Lighthouse](https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk?hl=en) was used to test the performance of the website. The website's performance received relatively lower scores, primarily due to its extensive use of images. However, the accessibility, adherence to best practices, and SEO aspects consistently received high scores.

**Google Lighthouse results:**
<details>
<summary>Desktop</summary>
<img src="static/docs/lighthouse-desktop.png" width="60%">
</details>
<details>
<summary>Mobile</summary>
<img src="static/docs/lighthouse-mobile.png" width="60%">
</details>

# Accessibility
[The WAVE WebAIM](https://wave.webaim.org) web accessibility evaluation tool to check if the website meets strong accessibility standards.
As a result, I've identified several areas where I can work on improving the website's accessibility. Specifically, there are some contrast errors related to buttons that need enhancements to improve color contrast. Additionally, there are issues related to alerts, where links lead to the same page. These areas need my attention to make the website more user-friendly and accessible, ensuring a better experience for all visitors.

**Wave results:**
<details>
<summary>Home page</summary>
<img src="static/docs/wave.png" width="60%">
</details>

# Code validation

## HTML Validation
The [W3C Markup Validation Service](https://validator.w3.org/) was used to validate the HTML of the website.

**HTML Results:**

The following pages have been tested, and no errors were detected on any of them. However, an informational message (info) was encountered, which does not indicate an error but provides information about the HTML structure on certain pages. The message pertains to the use of trailing slashes on void elements.

<details>
<summary>Home page</summary>
<img src="static/docs/html-home.png" width="60%">
</details>
<details>
<summary>Products page</summary>
<img src="static/docs/html-products.png" width="60%">
</details>
<details>
<summary>Product detail page</summary>
<img src="static/docs/html-product-detail.png" width="60%">
</details>
<details>
<summary>News page</summary>
<img src="static/docs/html-news.png" width="60%">
</details>
<details>
<summary>Details page</summary>
<img src="static/docs/html-detials.png" width="60%">
</details>
<details>
<summary>Textile page</summary>
<img src="static/docs/html-textile.png" width="60%">
</details>
<details>
<summary>Textile page</summary>
<img src="static/docs/html-textile.png" width="60%">
</details>
<details>
<summary>Kitchen page</summary>
<img src="static/docs/html-kitchen.png" width="60%">
</details>
<details>
<summary>Lights page</summary>
<img src="static/docs/html-lights.png" width="60%">
</details>
<details>
<summary>Sale page</summary>
<img src="static/docs/html-sale.png" width="60%">
</details>
<details>
<summary>Checkout page</summary>
<img src="static/docs/html-checkout.png" width="60%">
</details>
<details>
<summary>Checkout success page</summary>
<img src="static/docs/html-checkout-success.png" width="60%">
</details>
<details>
<summary>Login page</summary>
<img src="static/docs/html-login.png" width="60%">
</details>
<details>
<summary>Sign up page</summary>
<img src="static/docs/html-signup.png" width="60%">
</details>
<details>
<summary>Logout page</summary>
<img src="static/docs/html-logout.png" width="60%">
</details>
<details>
<summary>Product Management: Add product page</summary>
<img src="static/docs/html-product-management-add.png" width="60%">
</details>
<details>
<summary>Product Management: Edit product page</summary>
<img src="static/docs/html-product-management-edit.png" width="60%">
</details>
<details>
<summary>My profile</summary>
<img src="static/docs/html-profile.png" width="60%">
</details>
<details>
<summary>Order history</summary>
<img src="static/docs/html-order-history.png" width="60%">
</details>
<details>
<summary>Favorite products page</summary>
<img src="static/docs/html-favorites.png" width="60%">
</details>
<details>
<summary>Contact page</summary>
<img src="static/docs/html-contact.png" width="60%">
</details>
<details>
<summary>Policy page</summary>
<img src="static/docs/html-policy.png" width="60%">
</details>

## CSS Validation
The [W3C Jigsaw CSS Validation Service](https://jigsaw.w3.org/css-validator/) was used to validate the CSS of the website.

**CSS results:**

The CSS was tested, and no errors were found.

<details>
<summary>base.css</summary>
<img src="static/docs/css-validation.png" width="60%">
</details>
<details>
<summary>checkout.css</summary>
<img src="static/docs/css-validation-checkout.png" width="60%">
</details>

## JS Validation
[JSHint](https://jshint.com/) was used to validate the JavaScript of the website

**JS results:**

The JS was tested, and no errors were found.

<details>
<summary>JS base template</summary>
<img src="static/docs/js-base-template.png" width="60%">
</details>
<details>
<summary>JS bag template</summary>
<img src="static/docs/js-bag.png" width="60%">
</details>
<details>
<summary>JS Stripe element</summary>
<img src="static/docs/js-stripe-element.png" width="60%">
</details>
<details>
<summary>JS Product management page: Add/Edit product</summary>
<img src="static/docs/js-add-edit-page.png" width="60%">
</details>
<details>
<summary>JS Newsletter</summary>
<img src="static/docs/js-newsletter.png" width="60%">
</details>

## Python validation
The Python code was tested using [Flake8](https://flake8.pycqa.org/en/latest/).

# Testing

## Manual testing
BDD, or Behaviour Driven Development, is the process used to test user stories in a non-technical way, allowing anyone to test the features of an app.

# Automated Testing

# Browser Testing

# Bugs and Fixes

| **Bug**                                                                                                                                                      | **Fix**                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Bug                 | Fix
