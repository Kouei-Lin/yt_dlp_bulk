#!/bin/zsh

# Name of the text file containing YouTube URLs
url_file="yt_url.txt"

# Create an output folder for downloaded videos
output_folder="video"

# Create the output folder if it doesn't exist
mkdir -p "$output_folder"

# Loop through each URL in the text file and download the video
while IFS= read -r url
do
    yt-dlp -o "$output_folder/%(title)s.%(ext)s" "$url"
done < "$url_file"
