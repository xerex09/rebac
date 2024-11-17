  import React, { useCallback, useMemo } from 'react';
  import ReactFlow, {
    Background,
    Controls,
    Handle,
    Position,
    Node,
    Edge,
    NodeProps,
    MiniMap,
  } from 'reactflow';
  import 'reactflow/dist/style.css';
  import { Resource } from '../App';

  // Custom node component
  const ResourceNode: React.FC<NodeProps> = ({ data }) => {
    return (
      <div className="px-4 py-2 shadow-md rounded-md bg-white border-2 border-gray-200">
        <Handle type="target" position={Position.Top} className="w-2 h-2" />
        <div className="flex flex-col">
          <div className="font-bold text-sm">{data.name}</div>
          <div className="text-xs text-gray-500">
            Roles: {Object.keys(data.roles).join(', ')}
          </div>
        </div>
        <Handle type="source" position={Position.Bottom} className="w-2 h-2" />
      </div>
    );
  };

  const nodeTypes = {
    resource: ResourceNode,
  };

  const PolicyGraph: React.FC<{ resources: Resource[] }> = ({ resources }) => {

    console.log(resources);
    // Transform resources into nodes and edges
    const { nodes, edges } = useMemo(() => {
      const nodes: Node[] = resources.map((resource, index) => ({
        id: resource.id,
        type: 'resource',
        position: {
          x: 250 * Math.cos((2 * Math.PI * index) / resources.length),
          y: 250 * Math.sin((2 * Math.PI * index) / resources.length),
        },
        data: {
          name: resource.name,
          roles: resource.roles,
          actions: resource.actions,
        },
      }));

      const edges: Edge[] = [];
      resources.forEach(resource => {
        Object.entries(resource.relations).forEach(([relationKey, relation]) => {
          edges.push({
            id: `${resource.id}-${relation.resource_id}-${relationKey}`,
            source: resource.id,
            target: relation.resource_id,
            label: relationKey,
            type: 'smoothstep',
            animated: false,
            style: { stroke: '#64748b' },
          });
        });
      });
      console.log(nodes);
      return { nodes, edges };
    }, [resources]);

    // Handle node click
    const onNodeClick = useCallback((event: React.MouseEvent, node: Node) => {
      console.log('Node clicked:', node);

    }, []);

    return (
      <div style={{ height: '80vh', width: '100%' }}>
        <ReactFlow
          nodes={nodes}
          edges={edges}
          nodeTypes={nodeTypes}
          onNodeClick={onNodeClick}
          fitView
          defaultEdgeOptions={{
            type: 'smoothstep',
            style: { strokeWidth: 2 },
          }}
        >
          <Background />
          <Controls />
          <MiniMap />
        </ReactFlow>
      </div>
    );
  };

  export default PolicyGraph;