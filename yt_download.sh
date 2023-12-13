#!/bin/zsh

# Name of the text file containing YouTube URLs
url_file="yt_url.txt"

# Create an output folder for downloaded videos
output_folder="video"

# Create the output folder if it doesn't exist
mkdir -p "$output_folder"

# Function to download a single video
download_video() {
    local url="$1"
    yt-dlp -o "$output_folder/%(title)s.%(ext)s" "$url"
}

# Export the function to make it available to parallel
export -f download_video

# Use parallel to download videos in parallel
cat "$url_file" | parallel -j4 download_video

