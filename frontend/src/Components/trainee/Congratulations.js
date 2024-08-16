import React, { useState } from 'react';
import ReactStars from 'react-stars';

const Congratulations = ({ courseName, certificateUrl, onSubmitReview }) => {
  const [review, setReview] = useState('');
  const [rating, setRating] = useState(0);

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmitReview({ review, rating });
  };

  return (
    <div className="max-w-2xl mx-auto mt-10 p-6 bg-white rounded-lg shadow-xl">
      <h1 className="text-3xl font-bold text-center text-green-600 mb-6">
        Congratulations!
      </h1>
      <p className="text-xl text-center mb-6">
        You've successfully completed the course:
        <span className="font-semibold block mt-2">{courseName}</span>
      </p>
      
      <div className="mb-6">
        <h2 className="text-2xl font-semibold mb-3">Your Certificate</h2>
        <img 
          src={certificateUrl} 
          alt="Course Certificate" 
          className="w-full border-2 border-gray-300 rounded-lg"
        />
      </div>

      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <label htmlFor="review" className="block text-lg font-medium mb-2">
            Leave a Review
          </label>
          <textarea
            id="review"
            rows="4"
            className="w-full px-3 py-2 text-gray-700 border rounded-lg focus:outline-none"
            placeholder="Share your thoughts about the course..."
            value={review}
            onChange={(e) => setReview(e.target.value)}
          ></textarea>
        </div>

        <div>
          <label className="block text-lg font-medium mb-2">
            Rate the Course
          </label>
          <ReactStars
            count={5}
            onChange={setRating}
            size={24}
            color2={'#ffd700'}
            half={false}
          />
        </div>

        <button
          type="submit"
          className="w-full bg-blue-600 text-white py-2 px-4 rounded-lg hover:bg-blue-700 transition duration-300"
        >
          Submit Review
        </button>
      </form>
    </div>
  );
};


function CourseCompletion() {
  const handleReviewSubmit = (reviewData) => {
    // Handle the review submission, e.g., send to server
    console.log(reviewData);
  };

  return (
    <Congratulations
      courseName="Introduction to React"
      certificateUrl="https://cdn4.vectorstock.com/i/1000x1000/79/33/certification-icon-symbol-creative-sign-from-gdpr-vector-27647933.jpg"
      onSubmitReview={handleReviewSubmit}
    />
  );
}

export default CourseCompletion;