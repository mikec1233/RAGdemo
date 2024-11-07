import { DefaultApi } from "../api-client/apis"; // Import the generated API client
import { QueryRequest } from "../api-client/models"; // Import the necessary model type

// Define the interface for the API response
interface QueryResponse {
  answerText?: string; // Optional property as it may be undefined
}

// Initialize the DefaultApi instance
const api = new DefaultApi();

// Service function to submit the query
export const submitQuery = async (queryText: string): Promise<string> => {
  // Create a request body matching the `QueryRequest` type
  const requestBody: QueryRequest = {
    userInput: queryText, // Align with the defined structure in your models
  };

  try {
    // Call the generated API method and cast the response to `QueryResponse`
    const result = (await api.queryChatV1ChatQueryPost({ queryRequest: requestBody })) as QueryResponse;

    // Ensure to handle potential undefined values in the response
    return result.answerText ?? "No response"; // Use a default fallback message if `answerText` is undefined
  } catch (error) {
    // Improve error logging for better debugging
    console.error("Error submitting query:", error);
    throw new Error("Failed to submit the query. Please try again later.");
  }
};
