# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('udemy_courses_dataset.csv')

df = pd.read_csv("udemy_courses_dataset.csv")

numeric_columns = ["price", "num_subscribers", "num_reviews", "content_duration"]

# Generate summary statistics
summary_stats = df[numeric_columns].describe()

# Save the summary statistics to a CSV file
summary_stats.to_csv("summary_statistics.csv")

# Display the summary statistics
print("Summary Statistics for Key Numeric Columns:")
print(summary_stats)

# Visualizations for key numeric columns
for column in numeric_columns:
    plt.figure(figsize=(10, 6))
    sns.histplot(df[column], kde=True, bins=30, color="blue", edgecolor="black")
    plt.title(f'Distribution of {column.capitalize()}')
    plt.xlabel(column.capitalize())
    plt.ylabel('Frequency')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.savefig(f'{column}_distribution.png', dpi=300, bbox_inches='tight')
    plt.show()

# Pairplot for relationships among key numeric variables
sns.pairplot(df[numeric_columns], diag_kind="kde", corner=True)
plt.savefig("pairplot_numeric_columns.png", dpi=300, bbox_inches='tight')
plt.show()


## 1. Histogram for price distribution
# plt.figure(figsize=(8, 6))
# sns.histplot(data['price'], kde=True, bins=20)
# plt.xlabel('Course Price')  # Rename x-axis
# plt.ylabel('Frequency')  # Rename y-axis
# plt.title('Distribution of Course Prices')  # Add title
# plt.savefig('price_distribution.png')  # Save chart
# plt.show()  # Show the plot



# 2. Price vs Number of Subscribers
# plt.figure(figsize=(10, 6))
# sns.scatterplot(data=df, x="price", y="num_subscribers", alpha=0.6, color="blue")
# plt.title("Price vs Number of Subscribers")
# plt.xlabel("Price")
# plt.ylabel("Number of Subscribers")
# plt.grid()
# plt.savefig("price_vs_subscribers.png", dpi=300, bbox_inches="tight")
# plt.show()

# # Correlation coefficient
# correlation = df["price"].corr(df["num_subscribers"])
# print(f"Correlation coefficient between price and number of subscribers: {correlation}")

# 3. Top 10 Courses by Number of Subscribers
# top_10_courses = df.nlargest(10, "num_subscribers")[["course_title", "num_subscribers"]]
# plt.figure(figsize=(12, 6))
# sns.barplot(data=top_10_courses, x="num_subscribers", y="course_title", palette="viridis")
# plt.title("Top 10 Courses by Number of Subscribers")
# plt.xlabel("Number of Subscribers")
# plt.ylabel("Course Title")
# plt.savefig("top_10_courses.png", dpi=300, bbox_inches="tight")
# plt.show()

#4. Most Common Course Levels
# course_levels = df["level"].value_counts()
# plt.figure(figsize=(10, 6))
# sns.barplot(x=course_levels.index, y=course_levels.values, palette="pastel")
# plt.title("Most Common Course Levels")
# plt.xlabel("Course Level")
# plt.ylabel("Number of Courses")
# plt.savefig("common_course_levels.png", dpi=300, bbox_inches="tight")
# plt.show()

# # 5. Course Duration vs. Number of Reviews
# plt.figure(figsize=(10, 6))
# sns.scatterplot(data=df, x="content_duration", y="num_reviews", alpha=0.6, color="purple")
# plt.title("Course Duration vs Number of Reviews")
# plt.xlabel("Course Duration (hours)")
# plt.ylabel("Number of Reviews")
# plt.grid()
# plt.savefig("duration_vs_reviews.png", dpi=300, bbox_inches="tight")
# plt.show()

# 6. Subjects Analysis
# subject_counts = df["subject"].value_counts()
# plt.figure(figsize=(10, 6))
# sns.barplot(x=subject_counts.index, y=subject_counts.values, palette="coolwarm")
# plt.title("Subjects Analysis")
# plt.xlabel("Subject")
# plt.ylabel("Number of Courses")
# plt.savefig("subject_analysis.png", dpi=300, bbox_inches="tight")
# plt.show()