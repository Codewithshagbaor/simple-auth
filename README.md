# simple-auth

Simple Django + DRF authentication system using a custom user model and JWT (SimpleJWT).

## Overview

This project implements:
- Custom user model: [`User`]
- Registration and email-based login endpoints: [`base.views.UserRegistrationView`], [`base.views.EmailLoginView`]
- Serializers and token generation: [`base.serializers.LoginSerializer`]
- Email authentication backend: [`base.backends.EmailAuthenticationBackend`]
- Project settings: [`configs.settings`]

## Requirements

- Python 3.10+ (or your project's target)
- Django (>= 5.2)
- djangorestframework
- djangorestframework-simplejwt
- django-cors-headers