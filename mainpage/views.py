from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, timezone, timedelta

from mainpage.models import Post

posts = [Post(
    title="Post 1", author="FCA", creationdate=datetime.now(tz=timezone(-timedelta(hours=3))), updatedate=datetime.now(tz=timezone(-timedelta(hours=3))), organism="Cryptococcus neoformans", text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Purus in massa tempor nec feugiat nisl pretium fusce. Enim sed faucibus turpis in eu mi bibendum neque egestas. Id aliquet risus feugiat in ante metus dictum at tempor. Laoreet id donec ultrices tincidunt arcu non sodales neque sodales. Massa enim nec dui nunc mattis enim ut. Dolor sit amet consectetur adipiscing elit. Iaculis at erat pellentesque adipiscing commodo elit. Sed vulputate mi sit amet mauris commodo quis imperdiet massa. Suspendisse ultrices gravida dictum fusce ut placerat orci nulla. Praesent tristique magna sit amet purus gravida quis blandit turpis. Tincidunt tortor aliquam nulla facilisi cras. Ut tristique et egestas quis ipsum suspendisse ultrices gravida dictum. Mauris sit amet massa vitae tortor condimentum lacinia quis"
),
Post(
    title="Post 2", author="FCA", creationdate=datetime.now(tz=timezone(-timedelta(hours=3))), updatedate=datetime.now(tz=timezone(-timedelta(hours=3))), organism="Metarhizium anisopliae", text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Purus in massa tempor nec feugiat nisl pretium fusce. Enim sed faucibus turpis in eu mi bibendum neque egestas. Id aliquet risus feugiat in ante metus dictum at tempor. Laoreet id donec ultrices tincidunt arcu non sodales neque sodales. Massa enim nec dui nunc mattis enim ut. Dolor sit amet consectetur adipiscing elit. Iaculis at erat pellentesque adipiscing commodo elit. Sed vulputate mi sit amet mauris commodo quis imperdiet massa. Suspendisse ultrices gravida dictum fusce ut placerat orci nulla. Praesent tristique magna sit amet purus gravida quis blandit turpis. Tincidunt tortor aliquam nulla facilisi cras. Ut tristique et egestas quis ipsum suspendisse ultrices gravida dictum. Mauris sit amet massa vitae tortor condimentum lacinia quis"
),
Post(
    title="Post 3", author="FCA", creationdate=datetime.now(tz=timezone(-timedelta(hours=3))), updatedate=datetime.now(tz=timezone(-timedelta(hours=3))), organism="Cryptococcus neoformans", text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Purus in massa tempor nec feugiat nisl pretium fusce. Enim sed faucibus turpis in eu mi bibendum neque egestas. Id aliquet risus feugiat in ante metus dictum at tempor. Laoreet id donec ultrices tincidunt arcu non sodales neque sodales. Massa enim nec dui nunc mattis enim ut. Dolor sit amet consectetur adipiscing elit. Iaculis at erat pellentesque adipiscing commodo elit. Sed vulputate mi sit amet mauris commodo quis imperdiet massa. Suspendisse ultrices gravida dictum fusce ut placerat orci nulla. Praesent tristique magna sit amet purus gravida quis blandit turpis. Tincidunt tortor aliquam nulla facilisi cras. Ut tristique et egestas quis ipsum suspendisse ultrices gravida dictum. Mauris sit amet massa vitae tortor condimentum lacinia quis"
),
Post(
    title="Post 4", author="FCA", creationdate=datetime.now(tz=timezone(-timedelta(hours=3))), updatedate=datetime.now(tz=timezone(-timedelta(hours=3))), organism="Metarhizium anisopliae", text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Purus in massa tempor nec feugiat nisl pretium fusce. Enim sed faucibus turpis in eu mi bibendum neque egestas. Id aliquet risus feugiat in ante metus dictum at tempor. Laoreet id donec ultrices tincidunt arcu non sodales neque sodales. Massa enim nec dui nunc mattis enim ut. Dolor sit amet consectetur adipiscing elit. Iaculis at erat pellentesque adipiscing commodo elit. Sed vulputate mi sit amet mauris commodo quis imperdiet massa. Suspendisse ultrices gravida dictum fusce ut placerat orci nulla. Praesent tristique magna sit amet purus gravida quis blandit turpis. Tincidunt tortor aliquam nulla facilisi cras. Ut tristique et egestas quis ipsum suspendisse ultrices gravida dictum. Mauris sit amet massa vitae tortor condimentum lacinia quis"
)]


def home(request):
    return render(
        request,
        'mainpage/home.html',
        {'posts':posts}
    )