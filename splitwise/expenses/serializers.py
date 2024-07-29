from expenses.models import User, Expense, IndividualExpense, Type

from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return super().create(validated_data)
    class Meta:
        model = User
        exclude = ('last_login', )


class CreateUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    name = serializers.CharField()
    phone_number = PhoneNumberField()
    password = serializers.CharField()



class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('last_login', 'password')



class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = "__all__"


class IndividualExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndividualExpense
        fields = "__all__"


class CreateExpenseSerializer(serializers.Serializer):
    description = serializers.CharField(max_length=150)
    total_amount = serializers.IntegerField()
    type = serializers.ChoiceField(choices=Type)
    participants = serializers.ListField    ()
    participants_info = serializers.ListField()
    payed_by = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter())

