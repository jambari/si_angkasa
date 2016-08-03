from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
import datetime

from operasional.models import *
from tata_usaha.models import *

# Create your views here.
