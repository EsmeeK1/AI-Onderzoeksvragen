## Method/ Daily notes
This file will be used for logging progress and what i've tried/ learned.

### 11-9-2025
https://blogs.alisterluiz.com/zero-shot-text-classification-in-8-minutes-a-step-by-step-guide/: step by step walktrough can be found in -> `01_zero_shot_text_blog_alisterluiz.ipynb`
https://www.youtube.com/watch?v=cfly0OLldwg&embeds_referring_euri=https%3A%2F%2Fchatgpt.com%2F: step by step walktrough can be found in -> `02_zero_shot_text_youtube_endtoend.ipynb`

text zero-shot learning is quite simple in it's nature especially with pretrained models. Models already know sentiment from the training they've been through, so its relatively easy to ask them weather a movie review is "Positive" or "Negative" just by asking.

Besides that with zero-shot text classification you can also seperate between subject [sport, technology, health] etc. instead of sentiment.

### 14-9-2025
Applying zero-shot on image data is not that difficult when using pretrained models like CLIP. Essentially you're just calculating similarities between vectors (text vector and image vector) to see which one comes closest.

https://harrywang.me/clip: step by step walkthrough can be found in -> `03_zero_shot_image_CLIP.ipynb`

**Next Steps:**
- Explore **AudioCLIP / CLAP** to apply zero-shot techniques on audio projects.
- Potential tasks include zero-shot sound classification (*dog barking, car horn, rain*), audio-text retrieval (*“find clips of birds singing”*), and even speaker recognition.
- This directly aligns with our team’s focus on **sound-based projects**, making audio zero-shot learning a next research direction.

### 15-9-2025
Started reading a paper about AudioCLIP and zero-shot applications, decided to try to replicate the results
https://arxiv.org/pdf/2106.13043: step by step walkthrough can be found in -> `04_zero_shot_audio_CLIP.ipynb`

https://github.com/AndreyGuzhov/AudioCLIP.git