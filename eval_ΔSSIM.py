import os
import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim
import json
import argparse

# Function to calculate scores based on the test data and model output path
def calculate_scores(test_data, model_output_path):
    list_dir = []
    num = 0
    Holistic_Score = 0
    score_same = 0
    score_diff = 0

    # Traverse through the model output directory
    for _, dirs, _ in os.walk(model_output_path):
        for dir in dirs:
            # Find the corresponding test data for the current directory
            for ans in test_data:
                if ans['id'] == dir:
                    ans_figure_path = ans['Test_image']
                    ans_figure_initial_path = ans['Initial_figure']
                    break
            dir_path = os.path.join(model_output_path, dir)
            if os.path.isdir(dir_path):
                files = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]
                flag = 0
                # Look for the output PNG image (excluding Masked images)
                for file in files:
                    if file.endswith('.png') and not file.startswith('Masked'):
                        flag = 1
                        result_figure = cv2.imread(os.path.join(dir_path, file))
                        break
                if flag == 0:
                    continue
                # Read the answer and initial figures
                ans_figure = cv2.imread(ans_figure_path)
                initial_figure = cv2.imread(ans_figure_initial_path)
                try:
                    # Calculate SSIM index between answer and result figure
                    ssim_index_edit, _ = ssim(ans_figure, result_figure, full=True, channel_axis=-1)
                except:
                    try:
                        # Resize result image to match the size of the answer figure if dimensions don't match
                        height, width = ans_figure.shape[:2]
                        result_figure_resized = cv2.resize(result_figure, (width, height), interpolation=cv2.INTER_AREA)
                        ssim_index_edit, _ = ssim(ans_figure, result_figure_resized, full=True, channel_axis=-1)
                    except Exception as e:
                        print(f"Exception occurred in directory {dir}: {str(e)}")
                        continue
                # Calculate SSIM index between initial and answer figure
                ssim_index_initial, _ = ssim(initial_figure, ans_figure, full=True, channel_axis=-1)
                if ssim_index_edit == 1:
                    score = 100
                elif ssim_index_edit <= ssim_index_initial:
                    if ssim_index_edit == ssim_index_initial:
                        score_same += 1
                    else:
                        score_diff += 1
                        list_dir.append(dir)
                    score = 0
                else:
                    # Calculate score based on SSIM index
                    score = ((ssim_index_edit - ssim_index_initial) / (1 - ssim_index_initial)) * 100
                num += 1
                Holistic_Score += score

    return Holistic_Score, num, score_same, score_diff


def main():
    # Set up argument parser to take command-line inputs
    parser = argparse.ArgumentParser(description='Calculate scores for model outputs based on the test data.')
    parser.add_argument('test_path', type=str, help='Path to the test data JSON file.')
    parser.add_argument('model_output_path', type=str, help='Path to the directory containing model output images.')
    args = parser.parse_args()
    with open(args.test_path, 'r') as f:
        test_data = json.load(f)
    # Call the function to calculate scores
    holistic_score, num, score_same, score_diff = calculate_scores(test_data, args.model_output_path)

    # Print the results
    print(f"Holistic Score: {holistic_score / 1000}")
    print(f"Execute Rate: {num/1000}")
    #print(f"Number of identical scores: {score_same}")
    #print(f"Number of different scores: {score_diff}")
if __name__ == '__main__':
    main()
