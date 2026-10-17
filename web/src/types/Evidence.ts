export interface Evidence {
  id: string;
  finding_id: string;
  agent: string;
  tool: string;
  cypher: string;
  path: string[];
  claim: string;
}
