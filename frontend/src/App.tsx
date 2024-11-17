import React, { useEffect, useState } from 'react';
import axios from 'axios';
import PolicyGraph from './components/PolicyGraph';

// Define interfaces for the resource data structure
export interface Action {
  name: string;
  description: string | null;
  id: string;
  key: string;
}

export interface Role {
  name: string;
  description: string | null;
  permissions: string[];
  key: string;
  id: string;
}

export interface Resource {
  key: string;
  id: string;
  name: string;
  description: string | null;
  actions: Record<string, Action>;
  roles: Record<string, Role>;
  relations: Record<string, {
    description: string | null;
    resource_id: string;
    resource: string;
  }>;
}

const App: React.FC = () => {
  const [resources, setResources] = useState<Resource[]>([]);
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState<boolean>(true);

  const fetchData = async () => {
    try {
      setLoading(true);
      const resourcesRes = await axios.get<Resource[]>('http://localhost:8000/resources');
      setResources(resourcesRes.data);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An error occurred while fetching data.');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  return (
    <div className="min-h-screen bg-gray-50">
      <div className="container mx-auto px-4 py-8">
        <header className="mb-8">
          <h1 className="text-3xl font-bold text-gray-900 mb-2">
            ReBAC Policy Visualization
          </h1>
          <p className="text-gray-600">
            Interactive visualization of Resource-Based Access Control policies
          </p>
        </header>

        {loading ? (
          <div className="flex items-center justify-center h-64">
            <div className="text-xl text-gray-600">Loading policy data...</div>
          </div>
        ) : error ? (
          <div className="bg-red-50 border border-red-200 rounded-lg p-4">
            <p className="text-red-600">{error}</p>
            <button
              onClick={fetchData}
              className="mt-2 px-4 py-2 bg-red-100 text-red-700 rounded hover:bg-red-200"
            >
              Retry
            </button>
          </div>
        ) : (
          <div className="bg-white rounded-lg shadow-sm border p-4">
            <PolicyGraph resources={resources} />
          </div>
        )}
      </div>
    </div>
  );
};

export default App;