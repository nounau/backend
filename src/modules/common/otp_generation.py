import traceback
from flask import Flask, jsonify, request
import smtplib
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

load_dotenv();

class otp_generation:

    @staticmethod
    def generateOTP(mailObj, email):
        try:
            print("Under development")

            # return jsonify({'message': 'Email sent successfully', 'success': True}), 200

        except Exception as ex:
            traceback.print_exception(type(ex), ex, ex.__traceback__)
            # return jsonify({'message': 'Error occurred while sending email', 'success': False}), 500