from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils.translation import gettext_lazy as _


User = get_user_model()

class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super().__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

class UserSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = User
        exclude = ['is_staff', 'is_active', 'last_login', 'groups', 'user_permissions']
        write_only_fields = ['password']

    def create(self, validated_data):
        email = validated_data.get('email')
        password = validated_data.pop('password', None)
        
        if not email:
            raise serializers.ValidationError("Email must be provided.")
        user = User(**validated_data)
        if password:
            user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
    

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False)
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')

        password = data.get('password')

        if not email:
            raise serializers.ValidationError(_("Email must be provided."))

        user = authenticate(email=email, password=password)

        if user is None:
            raise serializers.ValidationError({"error":"Invalid credentials."})

        data['user'] = user
        return data

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
