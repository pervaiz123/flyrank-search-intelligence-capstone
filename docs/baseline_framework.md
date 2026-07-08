# Baseline Opportunity Scoring Framework

## Purpose

The baseline provides a simple, transparent method for identifying pages with optimization potential before introducing machine learning models.

## Assumption

Pages with high impressions but relatively poor ranking positions may represent strong optimization opportunities.

## Baseline Formula

Opportunity Score = Impressions / Average Position

## Interpretation

Higher scores indicate pages that receive significant visibility but may benefit from ranking improvements.

## Example

| Impressions | Position | Opportunity Score |
| ----------- | -------- | ----------------- |
| 10000       | 10       | 1000              |
| 5000        | 20       | 250               |
| 2000        | 5        | 400               |

## Usage

Pages will be ranked by Opportunity Score from highest to lowest.

## Role in the Capstone

The baseline will serve as the benchmark against which machine learning approaches are evaluated.
