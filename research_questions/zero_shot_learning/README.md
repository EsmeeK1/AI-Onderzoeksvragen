# Zero-Shot Learning
Learning sources:

- https://blogs.alisterluiz.com/zero-shot-text-classification-in-8-minutes-a-step-by-step-guide/
- https://www.youtube.com/watch?v=cfly0OLldwg

## Research Question
How can we perform classification without training data for the target classes, using pretrained models?

## Goals
- Understand the concept of zero-shot learning and its relation to pretrained models.
- Experiment with a simple implementation (text and image classification).
- Evaluate the benefits and limitations compared to supervised approaches.

## What is Zero-Shot Learning?
Zero-Shot learning is a method where you learn a model to correctly predict unlabeled data that it has never seen before. You don't train a model on a specific dataset, but you leverage a model pre-trained on a large set of data. What this means is that you can provide the model with a list of caniddate label, and it's gonna rank them according to how well they match the input text.

## Why use Zero-Shot Learning?
With classification, it usually requires a large labeled dataset. However in many cases this is hard to acquire, obtaining and labeling data is very time-consuming and expensive. That why, with zero-shot classification, you can bypass the need for that training phase. With zero shot you can:

- Test different labels or tasks without extensive preparation
- In the context of LLM's you can use it for sentiment analysis, topic detection or content moderation.
- There's no need to build and maintain large labeled datasets.

## Approach
- Start with a simple dataset (e.g., CIFAR-10 for images, or AG News for text).
- Use a pretrained model (e.g., CLIP for images, Hugging Face transformers for text).
- Compare zero-shot classification with a small supervised baseline.

## Experiments
- Zero-shot classification on facebook/bart-lage-mnli (`01_zero_shot_text_alisterluiz.ipynb`)
- Zero-shot classification on all-mpnet-base-v2 (`02_zero_shot_text_endtoend.ipynb`)
- Zero-shot classification with CLIP (`03_zero_shot_image_classification_CLIP.ipynb`)

## Results
- **Text (Rotten Tomatoes dataset):**
  - Accuracy ~78% with `all-mpnet-base-v2`.
  - Model showed a bias towards predicting *positive* reviews (high recall for positive, lower recall for negative).
  - Learned that **label phrasing** (“Positive sentiment” vs “A positive review”) can influence results.

- **Images (Unsplash dataset with CLIP):**
  - Zero-shot classification into *dawn/day/dusk/night* and *indoor/outdoor*.
  - Predictions were plausible overall (e.g., majority of photos marked *outdoor*).
  - Certain categories (e.g., *dusk*) were rarely predicted, showing either dataset imbalance or difficulty in distinguishing subtle classes. Could also mean the dataset does not contain alot of dusk-pictures, but did not dive into that question.

## Reflections
- **Strengths:**
  - Zero-shot learning is an interesting approach for prototyping and exploration.
  - It enables classification tasks without labeled data, which is valuable in domains where labels are scarce or costly.
  - Embedding-based similarity (cosine similarity) is a simple but effective mechanism.

- **Limitations:**
  - Sensitive to prompt wording, meaning results can vary with different phrasing.
  - Model biases become visible (e.g., preferring "day" or "positive").
  - Lack of ground truth in the image dataset made proper evaluation challenging.

- **Learnings:**
  - Understanding embeddings and cosine similarity is central to zero-shot learning.
  - Zero-shot can provide useful baselines but should be validated with domain-specific data.