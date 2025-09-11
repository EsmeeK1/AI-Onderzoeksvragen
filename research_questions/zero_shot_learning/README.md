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
- Zero-shot classification on facebook/bart-lage-mnli (`Bart_Large_Zero_Shot.ipynb`)
- Zero-shot classification on [youtube-dataset] TO:DO

## Results
(To be filled after experiments.)

## Reflections
(To be filled after experiments: What worked? What didn’t? What did I learn?)
